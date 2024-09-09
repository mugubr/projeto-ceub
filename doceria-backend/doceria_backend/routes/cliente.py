from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import Cliente, Usuario
from doceria_backend.schemas.cliente import (
    ClienteCreateSchema,
    ClienteDB,
    ClienteLista,
    ClienteSchema,
)
from doceria_backend.security import (
    get_admin,
    get_current_user,
    get_password_hash,
)

router = APIRouter(prefix='/clientes', tags=['Clientes'])


@router.get('/', response_model=ClienteLista)
def read_clientes(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    clientes = session.scalars(select(Cliente).limit(limit).offset(offset))
    return {'clientes': clientes}


@router.get('/{cliente_id}', response_model=ClienteDB)
def read_cliente(
    cliente_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    cliente = session.scalar(select(Cliente).where(Cliente.id == cliente_id))
    if not cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )
    return cliente


@router.post('/', response_model=ClienteDB, status_code=HTTPStatus.CREATED)
def create_cliente(
    novo_cliente: ClienteCreateSchema, session: Session = Depends(get_session)
):
    cliente = session.scalar(
        select(Cliente).where(
            (Cliente.celular == novo_cliente.celular)
            | (Cliente.email == novo_cliente.email)
        )
    )

    usuario_db = session.scalar(
        select(Usuario).where((Usuario.usuario == novo_cliente.usuario))
    )

    if usuario_db:
        if usuario_db.usuario == novo_cliente.usuario:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já cadastrado',
            )

    if cliente:
        if cliente.celular == novo_cliente.celular:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Celular já cadastrado',
            )
        if cliente.email == novo_cliente.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='E-mail já cadastrado',
            )

    novo_cliente_db = Cliente(
        nome=novo_cliente.nome,
        data_nascimento=novo_cliente.data_nascimento,
        celular=novo_cliente.celular,
        email=novo_cliente.email,
    )

    session.add(novo_cliente_db)
    session.commit()
    session.refresh(novo_cliente_db)

    cliente_db = session.scalar(
        select(Cliente).where(
            (Cliente.celular == novo_cliente_db.celular)
            | (Cliente.email == novo_cliente_db.email)
        )
    )

    novo_usuario = Usuario(
        usuario=novo_cliente.usuario,
        senha=get_password_hash(novo_cliente.senha),
        cliente_id=cliente_db.id,
    )

    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)

    return novo_cliente_db


@router.put('/{cliente_id}', response_model=ClienteDB)
def update_cliente(
    cliente_id: int,
    cliente: ClienteSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    if current_user.cliente_id != cliente_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Acesso negado'
        )

    cliente_db = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )
    if not cliente_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )

    cliente_erro = session.scalar(
        select(Cliente).where(
            (Cliente.celular == cliente.celular)
            | (Cliente.email == cliente.email)
        )
    )

    if cliente_erro:
        if cliente_erro.celular == cliente.celular:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Celular já cadastrado',
            )
        if cliente_erro.email == cliente.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='E-mail já cadastrado',
            )

    cliente_db.nome = cliente.nome
    cliente_db.data_nascimento = cliente.data_nascimento
    cliente_db.celular = cliente.celular
    cliente_db.email = cliente.email

    session.commit()
    session.refresh(cliente_db)

    return cliente_db


@router.delete('/{cliente_id}', response_model=dict)
def delete_cliente(
    cliente_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
    cliente_db = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )
    if not cliente_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )

    session.delete(cliente_db)
    session.commit()
    return {'message': 'Cliente deletado'}
