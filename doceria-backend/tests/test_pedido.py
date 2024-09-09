from datetime import datetime, timedelta
from http import HTTPStatus


def test_create_pedido(client, cliente, produto, token):
    response = client.post(
        '/pedidos',
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
        '/pedidos', headers={'Authorization': f'Bearer {token_admin}'}
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
                'nome': 'Cliente Teste',
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
                'nome': 'Cliente Teste',
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
        'nome': 'Cliente Teste',
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
