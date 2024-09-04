from datetime import datetime, timedelta
from http import HTTPStatus


def test_read_root_should_return_ok_and_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}


# CLIENTE
def test_create_cliente(client):
    response = client.post(
        '/clientes/',
        json={
            'nome': 'Cliente Teste',
            'data_nascimento': '1990-01-01',
            'celular': '11999999999',
            'email': 'cliente@teste.com',
            'usuario': 'teste',
            'senha': 'teste',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'nome': 'Cliente Teste',
        'data_nascimento': '1990-01-01',
        'celular': '11999999999',
        'email': 'cliente@teste.com',
    }


def test_read_clientes(client, cliente):
    response = client.get('/clientes/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'clientes': [
            {
                'id': 1,
                'nome': 'Cliente Teste',
                'data_nascimento': '1990-01-01',
                'celular': '11999999999',
                'email': 'cliente@teste.com',
            }
        ]
    }


def test_read_cliente(client, cliente):
    response = client.get('/clientes/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'nome': 'Cliente Teste',
        'data_nascimento': '1990-01-01',
        'celular': '11999999999',
        'email': 'cliente@teste.com',
    }


def test_read_cliente_should_return_404(client):
    response = client.get('/clientes/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


# def test_update_cliente(client, cliente):
#     response = client.put(
#         '/clientes/1',
#         json={
#             'nome': 'Cliente Teste Atualizado',
#             'data_nascimento': '1990-01-01',
#             'celular': '11999999999',
#             'email': 'cliente@atualizado.com',
#         },
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': 1,
#         'nome': 'Cliente Teste Atualizado',
#         'data_nascimento': '1990-01-01',
#         'celular': '11999999999',
#         'email': 'cliente@atualizado.com',
#     }


# def test_update_cliente_should_return_404(client, cliente):
#     response = client.put(
#         '/clientes/2',
#         json={
#             'nome': 'Cliente Teste Atualizado',
#             'data_nascimento': '1990-01-01',
#             'celular': '11999999999',
#             'email': 'cliente@atualizado.com',
#         },
#     )

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Cliente não encontrado'}


# def test_delete_cliente(client, cliente):
#     response = client.delete('/clientes/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'Cliente deletado'}


# def test_delete_cliente_should_return_404(client, cliente):
#     response = client.delete('/clientes/2')
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Cliente não encontrado'}


# USUARIO
def test_create_usuario(client, cliente):
    response = client.post(
        '/usuarios/',
        json={
            'usuario': 'testeuser',
            'senha': 'testepassword',
            'cliente_id': cliente.id,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'usuario': 'testeuser',
        'cliente_id': 1,
    }


def test_read_usuarios(client, usuario):
    response = client.get('/usuarios/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'usuarios': [
            {'id': usuario.id, 'usuario': usuario.usuario, 'cliente_id': 1}
        ]
    }


def test_read_usuario(client, usuario):
    response = client.get(f'/usuarios/{usuario.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': usuario.id,
        'usuario': usuario.usuario,
        'cliente_id': 1,
    }


def test_read_usuario_should_return_404(client):
    response = client.get('/usuarios/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


# def test_update_usuario(client, usuario):
#     response = client.put(
#         f'/usuarios/{usuario.id}',
#         json={
#             'usuario': 'updateduser',
#             'senha': 'updatedpassword',
#         },
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': usuario.id,
#         'usuario': 'updateduser',
#     }


# def test_update_usuario_should_return_404(client):
#     response = client.put(
#         '/usuarios/2',
#         json={
#             'usuario': 'updateduser',
#             'senha': 'updatedpassword',
#         },
#     )

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Usuário não encontrado'}


# def test_delete_usuario(client, usuario):
#     response = client.delete(f'/usuarios/{usuario.id}')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'Usuário deletado'}


# def test_delete_usuario_should_return_404(client):
#     response = client.delete('/usuarios/2')
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Usuário não encontrado'}


# PEDIDO
def test_create_pedido(client, cliente, produto):
    response = client.post(
        '/pedidos/',
        json={
            'data_entrega': (
                str((datetime.now() + timedelta(days=4)).date().isoformat())
            ),
            'ocasiao': 'Aniversário',
            'bairro': 'Centro',
            'logradouro': 'Rua Principal',
            'numero_complemento': '123',
            'ponto_referencia': 'Próximo ao mercado',
            'cliente_id': cliente.id,
            'produtos': [{'produto_id': produto.id, 'quantidade': 30}],
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'data_entrega': (
            str((datetime.now() + timedelta(days=4)).date().isoformat())
        ),
        'ocasiao': 'Aniversário',
        'bairro': 'Centro',
        'logradouro': 'Rua Principal',
        'numero_complemento': '123',
        'ponto_referencia': 'Próximo ao mercado',
        'cliente_id': cliente.id,
    }


def test_read_pedidos(client, pedido):
    response = client.get('/pedidos/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'pedidos': [
            {
                'id': 1,
                'cliente_id': 1,
                'data_entrega': str(datetime.now().date() + timedelta(days=4)),
                'ocasiao': 'Aniversário',
                'bairro': 'Centro',
                'logradouro': 'Rua Teste',
                'numero_complemento': '123',
                'ponto_referencia': 'Perto da escola',
                'valor': 250.0,
                'status': 'Em andamento',
                'celular': '11999999999',
                'descricao': '25X Produto Teste, ',
            }
        ]
    }


def test_read_pedido(client, pedido):
    response = client.get('/pedidos/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'cliente_id': 1,
        'data_entrega': str(datetime.now().date() + timedelta(days=4)),
        'ocasiao': 'Aniversário',
        'bairro': 'Centro',
        'logradouro': 'Rua Teste',
        'numero_complemento': '123',
        'ponto_referencia': 'Perto da escola',
        'valor': 250.0,
        'status': 'Em andamento',
        'celular': '11999999999',
        'descricao': '25X Produto Teste, ',
    }


def test_read_pedido_should_return_404(client):
    response = client.get('/pedidos/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Pedido não encontrado'}


# def test_update_pedido(client):
#     response = client.put(
#         '/pedidos/1',
#         json={
#             'data_entrega': '2023-09-01',
#             'ocasiao': 'Casamento',
#             'bairro': 'Jardim',
#             'logradouro': 'Rua Secundária',
#             'numero_complemento': '456',
#             'ponto_referencia': 'Em frente ao parque',
#         },
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': 1,
#         'cliente_id': 1,
#         'data_entrega': '2023-09-01',
#         'ocasiao': 'Casamento',
#         'bairro': 'Jardim',
#         'logradouro': 'Rua Secundária',
#         'numero_complemento': '456',
#         'ponto_referencia': 'Em frente ao parque',
#     }


# def test_update_pedido_should_return_404(client):
#     response = client.put(
#         '/pedidos/2',
#         json={
#             'data_entrega': '2023-09-01',
#             'ocasiao': 'Casamento',
#             'bairro': 'Jardim',
#             'logradouro': 'Rua Secundária',
#             'numero_complemento': '456',
#             'ponto_referencia': 'Em frente ao parque',
#         },
#     )

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Pedido não encontrado'}


# def test_delete_pedido(client):
#     response = client.delete('/pedidos/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'Pedido deletado'}


# def test_delete_pedido_should_return_404(client):
#     response = client.delete('/pedidos/2')
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Pedido não encontrado'}


# PRODUTO


def test_create_produto(client):
    response = client.post(
        '/produtos/',
        json={
            'nome': 'Bolo de Chocolate',
            'preco': 35.50,
            'tempo_producao': 120,
            'vegano': False,
            'gluten': True,
            'lactose': True,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'nome': 'Bolo de Chocolate',
        'preco': 35.50,
        'tempo_producao': 120,
        'vegano': False,
        'gluten': True,
        'lactose': True,
    }


def test_read_produtos(client, produto):
    response = client.get('/produtos/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'produtos': [
            {
                'id': 1,
                'nome': 'Produto Teste',
                'preco': 10.0,
                'tempo_producao': 1,
                'vegano': False,
                'gluten': True,
                'lactose': False,
            }
        ]
    }


def test_read_produto(client, produto):
    response = client.get('/produtos/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'nome': 'Produto Teste',
        'preco': 10.0,
        'tempo_producao': 1,
        'vegano': False,
        'gluten': True,
        'lactose': False,
    }


def test_read_produto_should_return_404(client):
    response = client.get('/produtos/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Produto não encontrado'}


# def test_update_produto(client):
#     response = client.put(
#         '/produtos/1',
#         json={
#             'nome': 'Bolo de Cenoura',
#             'preco': 30.00,
#             'tempo_producao': 90,
#             'vegano': True,
#             'gluten': False,
#             'lactose': False,
#         },
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': 1,
#         'nome': 'Bolo de Cenoura',
#         'preco': 30.00,
#         'tempo_producao': 90,
#         'vegano': True,
#         'gluten': False,
#         'lactose': False,
#     }


# def test_update_produto_should_return_404(client):
#     response = client.put(
#         '/produtos/2',
#         json={
#             'nome': 'Bolo de Cenoura',
#             'preco': 30.00,
#             'tempo_producao': 90,
#             'vegano': True,
#             'gluten': False,
#             'lactose': False,
#         },
#     )

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Produto não encontrado'}


# def test_delete_produto(client):
#     response = client.delete('/produtos/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'Produto deletado'}


# def test_delete_produto_should_return_404(client):
#     response = client.delete('/produtos/2')
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Produto não encontrado'}
