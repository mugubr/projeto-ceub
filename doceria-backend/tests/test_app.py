from http import HTTPStatus

from fastapi.testclient import TestClient

from doceria_backend.app import app


def test_read_root_should_return_ok_and_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo'}
