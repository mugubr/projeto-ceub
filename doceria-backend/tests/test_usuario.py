from http import HTTPStatus


def test_create_usuario(client, token_admin):
    response = client.post(
        '/usuarios',
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
    response = client.get('/usuarios')
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
