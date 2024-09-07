from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from doceria_backend.app import app
from doceria_backend.database import get_session
from doceria_backend.models import (
    Cliente,
    Mensagem,
    Pedido,
    PedidoProduto,
    Produto,
    Usuario,
    table_registry,
)
from doceria_backend.security import get_password_hash
from doceria_backend.settings import Settings


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )

    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def cliente(session: Session):
    cliente = Cliente(
        nome='Cliente Teste',
        data_nascimento=datetime.strptime('1990-01-01', '%Y-%m-%d').date(),
        celular='11999999999',
        email='cliente@teste.com',
    )
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente


@pytest.fixture
def usuario(session: Session, cliente: Cliente):
    pwd = 'senha_teste'
    usuario = Usuario(
        usuario='usuario_teste',
        senha=get_password_hash(pwd),
        cliente_id=cliente.id,
    )
    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    usuario.senha_limpa = pwd
    return usuario


@pytest.fixture
def admin(session: Session, cliente: Cliente):
    pwd = 'senha_teste'
    usuario = Usuario(
        usuario=Settings().ADMIN,
        senha=get_password_hash(pwd),
        cliente_id=cliente.id,
    )
    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    usuario.senha_limpa = pwd
    return usuario


@pytest.fixture
def produto(session: Session):
    produto = Produto(
        nome='Produto Teste',
        preco=10.0,
        tempo_producao=1,
        vegano=False,
        gluten=True,
        lactose=False,
    )
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto


@pytest.fixture
def pedido(session: Session, cliente: Cliente, produto: Produto):
    pedido = Pedido(
        data_entrega=datetime.now() + timedelta(days=4),
        ocasiao='Aniversário',
        bairro='Centro',
        logradouro='Rua Teste',
        numero_complemento='123',
        ponto_referencia='Perto da escola',
        cliente_id=cliente.id,
    )
    session.add(pedido)
    session.commit()
    session.refresh(pedido)

    pedido_produto = PedidoProduto(
        pedido_id=pedido.id, produto_id=produto.id, quantidade=25
    )
    session.add(pedido_produto)
    session.commit()
    session.refresh(pedido_produto)

    return pedido


@pytest.fixture
def token(client, usuario):
    response = client.post(
        '/auth/token',
        data={'username': usuario.usuario, 'password': usuario.senha_limpa},
    )
    return response.json()['access_token']


@pytest.fixture
def token_admin(client, admin):
    response = client.post(
        '/auth/token',
        data={'username': admin.usuario, 'password': admin.senha_limpa},
    )
    return response.json()['access_token']


@pytest.fixture
def mensagem(session: Session):
    mensagem = Mensagem(
        mensagem='mensagem teste',
    )
    session.add(mensagem)
    session.commit()
    session.refresh(mensagem)

    return mensagem
