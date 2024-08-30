from sqlalchemy import select

from doceria_backend.models import Usuario


def test_create_user(session):
    usuario = Usuario(usuario='teste', senha='teste', cliente_id=1)

    session.add(usuario)
    session.commit()
    resultado = session.scalar(
        select(Usuario).where(Usuario.usuario == 'teste')
    )

    assert resultado.usuario == usuario.usuario
    assert resultado.senha == usuario.senha
    assert resultado.cliente_id == usuario.cliente_id
