from http import HTTPStatus


def test_create_produto(client, token_admin):
    response = client.post(
        '/produtos',
        headers={'Authorization': f'Bearer {token_admin}'},
        json={
            'nome': 'Bolo de Chocolate',
            'preco': 35.50,
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
        'vegano': False,
        'gluten': True,
        'lactose': True,
    }


def test_read_produtos(client, produto, token):
    response = client.get(
        '/produtos',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'produtos': [
            {
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
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
