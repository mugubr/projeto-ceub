from http import HTTPStatus

import pywhatkit as whatsapp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import Mensagem
from doceria_backend.schemas.mensagem import (
    MensagemCreateSchema,
    MensagemLista,
    MensagemSchema,
    MensagemUpdateSchema,
)
from doceria_backend.security import get_admin

router = APIRouter(prefix='/mensagens', tags=['Mensagens'])


@router.get('/', response_model=MensagemLista)
def read_mensagens(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    mensagens = session.scalars(select(Mensagem).limit(limit).offset(offset))
    return {'mensagens': mensagens}


@router.get('/{mensagem_id}', response_model=MensagemSchema)
def read_mensagem(
    mensagem_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    mensagem = session.scalar(
        select(Mensagem).where(Mensagem.id == mensagem_id)
    )
    if not mensagem:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Mensagem não encontrada'
        )
    return mensagem


@router.get(
    '/enviar/{numero}/{mensagem_id}',
    status_code=HTTPStatus.OK,
    response_model=dict,
)
def envia_mensagem_whatsapp(
    numero: str,
    mensagem_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    numero_formatado = '+55' + numero
    mensagem = session.scalar(
        select(Mensagem).where(Mensagem.id == mensagem_id)
    )
    if not mensagem:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Mensagem não encontrada'
        )

    mensagem = mensagem.mensagem

    whatsapp.sendwhatmsg_instantly(
        phone_no=numero_formatado, message=mensagem, tab_close=True
    )

    return {'message': 'Mensagem enviada com sucesso'}


@router.post(
    '/', response_model=MensagemSchema, status_code=HTTPStatus.CREATED
)
def create_mensagem(
    nova_mensagem: MensagemCreateSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    nova_mensagem_db = Mensagem(mensagem=nova_mensagem.mensagem)

    session.add(nova_mensagem_db)
    session.commit()
    session.refresh(nova_mensagem_db)

    return nova_mensagem_db


@router.put('/{mensagem_id}', response_model=MensagemSchema)
def update_mensagem(
    mensagem_id: int,
    mensagem: MensagemUpdateSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    mensagem_db = session.scalar(
        select(Mensagem).where(Mensagem.id == mensagem_id)
    )
    if not mensagem_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Mensagem não encontrada'
        )

    mensagem_db.mensagem = mensagem.mensagem

    session.commit()
    session.refresh(mensagem_db)

    return mensagem_db


@router.delete('/{mensagem_id}', response_model=dict)
def delete_mensagem(
    mensagem_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    mensagem_db = session.scalar(
        select(Mensagem).where(Mensagem.id == mensagem_id)
    )
    if not mensagem_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Mensagem não encontrada'
        )
    session.delete(mensagem_db)
    session.commit()
    return {'message': 'Mensagem deletada'}
