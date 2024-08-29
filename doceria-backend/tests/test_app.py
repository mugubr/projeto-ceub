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


def test_read_clientes(client):
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


def test_read_cliente(client):
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


def test_update_cliente(client):
    response = client.put(
        '/clientes/1',
        json={
            'nome': 'Cliente Teste Atualizado',
            'data_nascimento': '1990-01-01',
            'celular': '11999999999',
            'email': 'cliente@atualizado.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'nome': 'Cliente Teste Atualizado',
        'data_nascimento': '1990-01-01',
        'celular': '11999999999',
        'email': 'cliente@atualizado.com',
    }


def test_update_cliente_should_return_404(client):
    response = client.put(
        '/clientes/2',
        json={
            'nome': 'Cliente Teste Atualizado',
            'data_nascimento': '1990-01-01',
            'celular': '11999999999',
            'email': 'cliente@atualizado.com',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


def test_delete_cliente(client):
    response = client.delete('/clientes/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Cliente deletado'}


def test_delete_cliente_should_return_404(client):
    response = client.delete('/clientes/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


# USUARIO
def test_create_usuario(client):
    response = client.post(
        '/usuarios/',
        json={
            'usuario': 'testeuser',
            'senha': 'testepassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'usuario': 'testeuser',
    }


def test_read_usuarios(client):
    response = client.get('/usuarios/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'usuarios': [
            {
                'id': 1,
                'usuario': 'testeuser',
            }
        ]
    }


def test_read_usuario(client):
    response = client.get('/usuarios/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'usuario': 'testeuser',
    }


def test_read_usuario_should_return_404(client):
    response = client.get('/usuarios/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_update_usuario(client):
    response = client.put(
        '/usuarios/1',
        json={
            'usuario': 'updateduser',
            'senha': 'updatedpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'usuario': 'updateduser',
    }


def test_update_usuario_should_return_404(client):
    response = client.put(
        '/usuarios/2',
        json={
            'usuario': 'updateduser',
            'senha': 'updatedpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_usuario(client):
    response = client.delete('/usuarios/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Usuário deletado'}


def test_delete_usuario_should_return_404(client):
    response = client.delete('/usuarios/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


# PEDIDO
def test_create_pedido(client):
    response = client.post(
        '/pedidos/',
        json={
            'data_entrega': '2023-08-28',
            'ocasiao': 'Aniversário',
            'bairro': 'Centro',
            'logradouro': 'Rua Principal',
            'numero_complemento': '123',
            'ponto_referencia': 'Próximo ao mercado',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'cliente_id': 1,
        'data_entrega': '2023-08-28',
        'ocasiao': 'Aniversário',
        'bairro': 'Centro',
        'logradouro': 'Rua Principal',
        'numero_complemento': '123',
        'ponto_referencia': 'Próximo ao mercado',
    }


def test_read_pedidos(client):
    response = client.get('/pedidos/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'pedidos': [
            {
                'id': 1,
                'cliente_id': 1,
                'data_entrega': '2023-08-28',
                'ocasiao': 'Aniversário',
                'bairro': 'Centro',
                'logradouro': 'Rua Principal',
                'numero_complemento': '123',
                'ponto_referencia': 'Próximo ao mercado',
            }
        ]
    }


def test_read_pedido(client):
    response = client.get('/pedidos/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'cliente_id': 1,
        'data_entrega': '2023-08-28',
        'ocasiao': 'Aniversário',
        'bairro': 'Centro',
        'logradouro': 'Rua Principal',
        'numero_complemento': '123',
        'ponto_referencia': 'Próximo ao mercado',
    }


def test_read_pedido_should_return_404(client):
    response = client.get('/pedidos/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Pedido não encontrado'}


def test_update_pedido(client):
    response = client.put(
        '/pedidos/1',
        json={
            'data_entrega': '2023-09-01',
            'ocasiao': 'Casamento',
            'bairro': 'Jardim',
            'logradouro': 'Rua Secundária',
            'numero_complemento': '456',
            'ponto_referencia': 'Em frente ao parque',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'cliente_id': 1,
        'data_entrega': '2023-09-01',
        'ocasiao': 'Casamento',
        'bairro': 'Jardim',
        'logradouro': 'Rua Secundária',
        'numero_complemento': '456',
        'ponto_referencia': 'Em frente ao parque',
    }


def test_update_pedido_should_return_404(client):
    response = client.put(
        '/pedidos/2',
        json={
            'data_entrega': '2023-09-01',
            'ocasiao': 'Casamento',
            'bairro': 'Jardim',
            'logradouro': 'Rua Secundária',
            'numero_complemento': '456',
            'ponto_referencia': 'Em frente ao parque',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Pedido não encontrado'}


def test_delete_pedido(client):
    response = client.delete('/pedidos/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Pedido deletado'}


def test_delete_pedido_should_return_404(client):
    response = client.delete('/pedidos/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Pedido não encontrado'}


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


def test_read_produtos(client):
    response = client.get('/produtos/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'produtos': [
            {
                'id': 1,
                'nome': 'Bolo de Chocolate',
                'preco': 35.50,
                'tempo_producao': 120,
                'vegano': False,
                'gluten': True,
                'lactose': True,
            }
        ]
    }


def test_read_produto(client):
    response = client.get('/produtos/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'nome': 'Bolo de Chocolate',
        'preco': 35.50,
        'tempo_producao': 120,
        'vegano': False,
        'gluten': True,
        'lactose': True,
    }


def test_read_produto_should_return_404(client):
    response = client.get('/produtos/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Produto não encontrado'}


def test_update_produto(client):
    response = client.put(
        '/produtos/1',
        json={
            'nome': 'Bolo de Cenoura',
            'preco': 30.00,
            'tempo_producao': 90,
            'vegano': True,
            'gluten': False,
            'lactose': False,
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'nome': 'Bolo de Cenoura',
        'preco': 30.00,
        'tempo_producao': 90,
        'vegano': True,
        'gluten': False,
        'lactose': False,
    }


def test_update_produto_should_return_404(client):
    response = client.put(
        '/produtos/2',
        json={
            'nome': 'Bolo de Cenoura',
            'preco': 30.00,
            'tempo_producao': 90,
            'vegano': True,
            'gluten': False,
            'lactose': False,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Produto não encontrado'}


def test_delete_produto(client):
    response = client.delete('/produtos/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Produto deletado'}


def test_delete_produto_should_return_404(client):
    response = client.delete('/produtos/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Produto não encontrado'}
