from http import HTTPStatus


def test_create_cliente(client):
    response = client.post(
        '/clientes',
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
        '/clientes', headers={'Authorization': f'Bearer {token_admin}'}
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
        '/clientes/1',
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
