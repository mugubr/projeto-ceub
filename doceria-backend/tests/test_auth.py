from http import HTTPStatus


def test_get_token(client, usuario):
    response = client.post(
        '/auth/token',
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
        '/auth/token',
        data={
            'username': usuario.usuario,
            'password': usuario.senha_limpa + 'teste',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Usuário ou senha incorretos'}
