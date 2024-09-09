from http import HTTPStatus


def test_create_mensagem(client, token_admin):
    response = client.post(
        '/mensagens',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'mensagem': 'testeuser',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'mensagem': 'testeuser',
    }


def test_read_mensagens(client, mensagem, token_admin):
    response = client.get(
        '/mensagens',
        headers={'Authorization': f'Bearer {token_admin}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'mensagens': [
            {
                'id': 1,
                'mensagem': mensagem.mensagem,
            }
        ]
    }


def test_read_mensagem(client, mensagem, token_admin):
    response = client.get(
        f'/mensagens/{mensagem.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': mensagem.id,
        'mensagem': mensagem.mensagem,
    }


def test_read_mensagem_should_return_404(client, token_admin):
    response = client.get(
        '/mensagens/2',
        headers={'Authorization': f'Bearer {token_admin}'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Mensagem não encontrada'}


def test_update_mensagem(client, mensagem, token_admin):
    response = client.put(
        f'/mensagens/{mensagem.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'mensagem': 'updatemessage',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': mensagem.id,
        'mensagem': 'updatemessage',
    }


def test_update_mensagem_should_return_404(client, token_admin):
    response = client.put(
        '/mensagens/2',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'mensagem': 'updatemessage',
            'senha': 'updatedpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Mensagem não encontrada'}


def test_delete_mensagem(client, mensagem, token_admin):
    response = client.delete(
        f'/mensagens/{mensagem.id}',
        headers={'Authorization': f'Bearer {token_admin}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Mensagem deletada'}


def test_delete_mensagem_should_return_404(client, token_admin):
    response = client.delete(
        '/mensagens/2', headers={'Authorization': f'Bearer {token_admin}'}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Mensagem não encontrada'}
