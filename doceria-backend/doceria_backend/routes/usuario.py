from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import Usuario
from doceria_backend.schemas.usuario import (
    UsuarioCreateSchema,
    UsuarioLista,
    UsuarioPublico,
    UsuarioSchema,
)
from doceria_backend.security import get_current_user, get_password_hash

router = APIRouter(prefix='/usuarios', tags=['Usuários'])


@router.get('/', response_model=UsuarioLista)
def read_usuarios(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
):
    usuarios = session.scalars(select(Usuario).limit(limit).offset(offset))
    return {'usuarios': usuarios}


@router.get('/{usuario_id}', response_model=UsuarioPublico)
def read_usuario(
    usuario_id: int,
    session: Session = Depends(get_session),
):
    usuario = session.scalar(select(Usuario).where(Usuario.id == usuario_id))
    if not usuario:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    return usuario


@router.post(
    '/', response_model=UsuarioPublico, status_code=HTTPStatus.CREATED
)
def create_usuario(
    novo_usuario: UsuarioCreateSchema,
    session: Session = Depends(get_session),
):
    usuario = session.scalar(
        select(Usuario).where(
            (Usuario.usuario == novo_usuario.usuario)
            | (Usuario.cliente_id == novo_usuario.cliente_id)
        )
    )

    if usuario:
        if usuario.usuario == novo_usuario.usuario:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já cadastrado',
            )
        if usuario.cliente_id == novo_usuario.cliente_id:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Cliente já cadastrado',
            )

    novo_usuario_db = Usuario(
        usuario=novo_usuario.usuario,
        senha=get_password_hash(novo_usuario.senha),
        cliente_id=novo_usuario.cliente_id,
    )

    session.add(novo_usuario_db)
    session.commit()
    session.refresh(novo_usuario_db)

    return novo_usuario_db


@router.put('/{usuario_id}', response_model=UsuarioPublico)
def update_usuario(
    usuario_id: int,
    usuario: UsuarioSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    usuario_db = session.scalar(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    if not usuario_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    usuario_erro = session.scalar(
        select(Usuario).where((Usuario.usuario == usuario.usuario))
    )

    if usuario_erro:
        if usuario_erro.usuario == usuario.usuario:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já cadastrado',
            )

    usuario_db.usuario = usuario.usuario
    usuario_db.senha = usuario.senha

    session.commit()
    session.refresh(usuario_db)

    return usuario_db


@router.delete('/{usuario_id}', response_model=dict)
def delete_usuario(
    usuario_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    usuario_db = session.scalar(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    if not usuario_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    session.delete(usuario_db)
    session.commit()
    return {'message': 'Usuário deletado'}
