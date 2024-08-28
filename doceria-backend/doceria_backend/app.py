from http import HTTPStatus
from fastapi import FastAPI

app = FastAPI(title='API Katherine Corrales - Doceria')


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo'}
