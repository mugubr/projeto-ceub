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


def test_read_clientes(client, cliente, token_admin):
    response = client.get(
        '/clientes/', headers={'Authorization': f'Bearer {token_admin}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'clientes': [
            {
                'id': cliente.id,
                'nome': cliente.nome,
                'data_nascimento': cliente.data_nascimento.isoformat(),
                'celular': cliente.celular,
                'email': cliente.email,
            }
        ]
    }


def test_read_cliente(client, cliente, token_admin):
    response = client.get(
        f'/clientes/{cliente.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': cliente.id,
        'nome': cliente.nome,
        'data_nascimento': cliente.data_nascimento.isoformat(),
        'celular': cliente.celular,
        'email': cliente.email,
    }


def test_read_cliente_should_return_404(client, token_admin):
    response = client.get(
        '/clientes/2', headers={'Authorization': f'Bearer {token_admin}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


def test_update_cliente(client, cliente, token):
    response = client.put(
        f'/clientes/{cliente.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'nome': 'Cliente Teste Atualizado',
            'data_nascimento': '1990-01-01',
            'celular': '11999999998',
            'email': 'cliente@atualizado.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': cliente.id,
        'nome': 'Cliente Teste Atualizado',
        'data_nascimento': '1990-01-01',
        'celular': '11999999998',
        'email': 'cliente@atualizado.com',
    }


def test_delete_cliente(client, cliente, token_admin):
    response = client.delete(
        f'/clientes/{cliente.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Cliente deletado'}


def test_delete_cliente_should_return_404(client, token_admin):
    response = client.delete(
        '/clientes/2', headers={'Authorization': f'Bearer {token_admin}'}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


# USUARIO
def test_create_usuario(client, token_admin):
    response = client.post(
        '/usuarios/',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'usuario': 'testeuser',
            'senha': 'testepassword',
            'cliente_id': 2,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 2,
        'usuario': 'testeuser',
        'cliente_id': 2,
    }


def test_read_usuarios(client, usuario):
    response = client.get('/usuarios/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'usuarios': [
            {
                'id': 1,
                'usuario': usuario.usuario,
                'cliente_id': usuario.cliente_id,
            }
        ]
    }


def test_read_usuario(client, usuario):
    response = client.get(
        f'/usuarios/{usuario.id}',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'usuario': usuario.usuario,
        'cliente_id': usuario.cliente_id,
    }


def test_read_usuario_should_return_404(client):
    response = client.get('/usuarios/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_update_usuario(client, usuario, token_admin):
    response = client.put(
        f'/usuarios/{usuario.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'usuario': 'updateduser',
            'senha': 'updatedpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': usuario.id,
        'usuario': 'updateduser',
        'cliente_id': usuario.cliente_id,
    }


def test_update_usuario_should_return_404(client, token_admin):
    response = client.put(
        '/usuarios/2',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'usuario': 'updateduser',
            'senha': 'updatedpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_usuario(client, usuario, token_admin):
    response = client.delete(
        f'/usuarios/{usuario.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Usuário deletado'}


def test_delete_usuario_should_return_404(client, token_admin):
    response = client.delete(
        '/usuarios/2', headers={'Authorization': f'Bearer {token_admin}'}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


# PEDIDO
def test_create_pedido(client, cliente, produto, token):
    response = client.post(
        '/pedidos/',
        headers={'Authorization': f'Bearer {token}'},
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


def test_read_pedidos(client, pedido, token_admin):
    response = client.get(
        '/pedidos/', headers={'Authorization': f'Bearer {token_admin}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'pedidos': [
            {
                'id': pedido.id,
                'cliente_id': pedido.cliente_id,
                'data_entrega': pedido.data_entrega.isoformat(),
                'ocasiao': pedido.ocasiao,
                'bairro': pedido.bairro,
                'logradouro': pedido.logradouro,
                'numero_complemento': pedido.numero_complemento,
                'ponto_referencia': pedido.ponto_referencia,
                'valor': 250.0,
                'status': 'Em andamento',
                'celular': '11999999999',
                'descricao': '25X Produto Teste',
            }
        ]
    }


def test_read_pedidos_by_cliente(client, cliente, pedido, token):
    response = client.get(
        f'/pedidos/cliente/{cliente.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'pedidos': [
            {
                'id': pedido.id,
                'cliente_id': cliente.id,
                'data_entrega': pedido.data_entrega.isoformat(),
                'ocasiao': pedido.ocasiao,
                'bairro': pedido.bairro,
                'logradouro': pedido.logradouro,
                'numero_complemento': pedido.numero_complemento,
                'ponto_referencia': pedido.ponto_referencia,
                'valor': 250.0,
                'status': 'Em andamento',
                'celular': '11999999999',
                'descricao': '25X Produto Teste',
            }
        ]
    }


def test_read_pedidos_by_cliente_should_return_empty_list(
    client, cliente, token
):
    response = client.get(
        f'/pedidos/cliente/{cliente.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'pedidos': []}


def test_read_pedidos_mes(client, pedido, produto, token_admin):
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    response = client.get(
        f'/pedidos/mes/{mes_atual}?ano={ano_atual}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )

    assert response.status_code == HTTPStatus.OK
    data = response.json()

    assert data['ano'] == ano_atual
    assert data['mes'] == mes_atual
    assert len(data['pedidos']) > 0

    dia_criado = pedido.criado_em.day
    assert str(dia_criado) in data['pedidos']
    assert len(data['pedidos'][str(dia_criado)]) == 1

    assert data['pedidos'][str(dia_criado)][0]['ocasiao'] == pedido.ocasiao
    assert data['pedidos'][str(dia_criado)][0]['bairro'] == pedido.bairro
    assert data['pedidos'][str(dia_criado)][0]['logradouro'] == (
        pedido.logradouro
    )
    assert data['pedidos'][str(dia_criado)][0]['numero_complemento'] == (
        pedido.numero_complemento
    )
    assert data['pedidos'][str(dia_criado)][0]['ponto_referencia'] == (
        pedido.ponto_referencia
    )
    assert data['pedidos'][str(dia_criado)][0]['valor'] == (produto.preco * 25)
    assert data['pedidos'][str(dia_criado)][0]['status'] == 'Em andamento'
    assert data['pedidos'][str(dia_criado)][0]['descricao'] == (
        f'25X {produto.nome}'
    )


def test_read_pedidos_by_mes_should_return_404(client, token_admin):
    ano_atual = datetime.now().year
    mes_vazio = (datetime.now().month + 1) % 12 or 12

    response = client.get(
        f'/pedidos/mes/{mes_vazio}?ano={ano_atual}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Nenhum pedido encontrado'}


def test_read_pedido(client, pedido, token_admin):
    response = client.get(
        f'/pedidos/{pedido.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': pedido.id,
        'cliente_id': pedido.cliente_id,
        'data_entrega': pedido.data_entrega.isoformat(),
        'ocasiao': pedido.ocasiao,
        'bairro': pedido.bairro,
        'logradouro': pedido.logradouro,
        'numero_complemento': pedido.numero_complemento,
        'ponto_referencia': pedido.ponto_referencia,
        'valor': 250.0,
        'status': 'Em andamento',
        'celular': '11999999999',
        'descricao': '25X Produto Teste',
    }


def test_read_pedido_should_return_404(client, token_admin):
    response = client.get(
        '/pedidos/2', headers={'Authorization': f'Bearer {token_admin}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Pedido não encontrado'}


def test_update_pedido(client, pedido, token):
    response = client.put(
        f'/pedidos/{pedido.id}',
        headers={'Authorization': f'Bearer {token}'},
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
        'id': pedido.id,
        'cliente_id': pedido.cliente_id,
        'data_entrega': '2023-09-01',
        'ocasiao': 'Casamento',
        'bairro': 'Jardim',
        'logradouro': 'Rua Secundária',
        'numero_complemento': '456',
        'ponto_referencia': 'Em frente ao parque',
    }


def test_update_pedido_should_return_404(client, token):
    response = client.put(
        '/pedidos/2',
        headers={'Authorization': f'Bearer {token}'},
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


def test_delete_pedido(client, pedido, token):
    response = client.delete(
        f'/pedidos/{pedido.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Pedido deletado'}


def test_delete_pedido_should_return_404(client, token):
    response = client.delete(
        '/pedidos/2',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Pedido não encontrado'}


# PRODUTO


def test_create_produto(client, token_admin):
    response = client.post(
        '/produtos/',
        headers={'Authorization': f'Bearer {token_admin}'},
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


def test_read_produtos(client, produto, token):
    response = client.get(
        '/produtos/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'produtos': [
            {
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
                'tempo_producao': produto.tempo_producao,
                'vegano': produto.vegano,
                'gluten': produto.gluten,
                'lactose': produto.lactose,
            }
        ]
    }


def test_read_produto(client, produto, token):
    response = client.get(
        '/produtos/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': produto.id,
        'nome': produto.nome,
        'preco': produto.preco,
        'tempo_producao': produto.tempo_producao,
        'vegano': produto.vegano,
        'gluten': produto.gluten,
        'lactose': produto.lactose,
    }


def test_read_produto_should_return_404(client, token):
    response = client.get(
        '/produtos/2', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Produto não encontrado'}


def test_update_produto(client, produto, token_admin):
    response = client.put(
        f'/produtos/{produto.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
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
        'id': produto.id,
        'nome': 'Bolo de Cenoura',
        'preco': 30.00,
        'tempo_producao': 90,
        'vegano': True,
        'gluten': False,
        'lactose': False,
    }


def test_update_produto_should_return_404(client, token_admin):
    response = client.put(
        '/produtos/2',
        headers={'Authorization': f'Bearer {token_admin}'},
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


def test_delete_produto(client, produto, token_admin):
    response = client.delete(
        f'/produtos/{produto.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Produto deletado'}


def test_delete_produto_should_return_404(client, token_admin):
    response = client.delete(
        '/produtos/2', headers={'Authorization': f'Bearer {token_admin}'}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Produto não encontrado'}


def test_get_token(client, usuario):
    response = client.post(
        '/token',
        data={
            'username': usuario.usuario,
            'password': usuario.senha_limpa,
        },
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert token['access_token']


def test_get_token_should_return_400(client, usuario):
    response = client.post(
        '/token',
        data={
            'username': usuario.usuario,
            'password': usuario.senha_limpa + 'teste',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Usuário ou senha incorretos'}
