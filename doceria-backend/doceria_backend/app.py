from http import HTTPStatus

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from doceria_backend.routes.auth import router as auth_router
from doceria_backend.routes.cliente import router as cliente_router
from doceria_backend.routes.mensagem import router as mensagem_router
from doceria_backend.routes.pedido import router as pedido_router
from doceria_backend.routes.produto import router as produto_router

app = FastAPI(title='API Katherine Corrales - Doceria')

app.include_router(mensagem_router)
app.include_router(auth_router)
app.include_router(cliente_router)
app.include_router(pedido_router)
app.include_router(produto_router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo'}
