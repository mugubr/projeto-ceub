from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import Usuario
from doceria_backend.security import create_access_token, verify_password

router = APIRouter(prefix='/auth', tags=['Autenticação'])


@router.post('/token')
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    usuario = session.scalar(
        select(Usuario).where(Usuario.usuario == form_data.username)
    )

    if not usuario or not verify_password(form_data.password, usuario.senha):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Usuário ou senha incorretos',
        )

    access_token = create_access_token(data={'sub': usuario.usuario})

    return {'access_token': access_token, 'token_type': 'Bearer'}
