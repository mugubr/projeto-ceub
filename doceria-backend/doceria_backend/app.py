from datetime import datetime
from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from doceria_backend.schemas.cliente import (
    ClienteDB,
    ClienteLista,
    ClienteSchema,
)
from doceria_backend.schemas.pedido import (
    PedidoDB,
    PedidoDBData,
    PedidoLista,
    PedidoSchema,
)
from doceria_backend.schemas.produto import (
    ProdutoDB,
    ProdutoLista,
    ProdutoSchema,
)
from doceria_backend.schemas.usuario import (
    UsuarioDB,
    UsuarioLista,
    UsuarioPublico,
    UsuarioSchema,
)

app = FastAPI(title='API Katherine Corrales - Doceria')


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo'}


# CLIENTE
database_clientes = []


@app.get('/clientes/', response_model=ClienteLista)
def read_clientes():
    return {'clientes': database_clientes}


@app.get('/clientes/{cliente_id}', response_model=ClienteDB)
def read_cliente(cliente_id: int):
    if cliente_id > len(database_clientes) or cliente_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )
    return database_clientes[cliente_id - 1]


@app.post(
    '/clientes/', response_model=ClienteDB, status_code=HTTPStatus.CREATED
)
def create_cliente(cliente: ClienteSchema):
    novo_cliente = ClienteDB(
        id=len(database_clientes) + 1, **cliente.model_dump()
    )
    database_clientes.append(novo_cliente)
    return novo_cliente


@app.put('/clientes/{cliente_id}', response_model=ClienteDB)
def update_cliente(cliente_id: int, cliente: ClienteSchema):
    if cliente_id > len(database_clientes) or cliente_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )

    cliente_atualizado = ClienteDB(id=cliente_id, **cliente.model_dump())
    database_clientes[cliente_id - 1] = cliente_atualizado
    return cliente_atualizado


@app.delete('/clientes/{cliente_id}', response_model=dict)
def delete_cliente(cliente_id: int):
    if cliente_id < 1 or cliente_id > len(database_clientes):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )

    del database_clientes[cliente_id - 1]
    return {'message': 'Cliente deletado'}


# USUARIO
database_usuarios = []


@app.get('/usuarios/', response_model=UsuarioLista)
def read_usuarios():
    return {'usuarios': database_usuarios}


@app.get('/usuarios/{usuario_id}', response_model=UsuarioPublico)
def read_usuario(usuario_id: int):
    if usuario_id > len(database_usuarios) or usuario_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    return database_usuarios[usuario_id - 1]


@app.post(
    '/usuarios/', response_model=UsuarioPublico, status_code=HTTPStatus.CREATED
)
def create_usuario(usuario: UsuarioSchema):
    novo_usuario = UsuarioDB(
        id=len(database_usuarios) + 1,
        cliente_id=len(database_usuarios) + 1,
        **usuario.model_dump(),
    )
    database_usuarios.append(novo_usuario)
    return novo_usuario


@app.put('/usuarios/{usuario_id}', response_model=UsuarioPublico)
def update_usuario(usuario_id: int, usuario: UsuarioSchema):
    if usuario_id > len(database_usuarios) or usuario_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    cliente_id_usuario = database_usuarios[usuario_id - 1].cliente_id
    usuario_atualizado = UsuarioDB(
        id=usuario_id, cliente_id=cliente_id_usuario, **usuario.model_dump()
    )
    database_usuarios[usuario_id - 1] = usuario_atualizado
    return usuario_atualizado


@app.delete('/usuarios/{usuario_id}', response_model=dict)
def delete_usuario(usuario_id: int):
    if usuario_id < 1 or usuario_id > len(database_usuarios):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    del database_usuarios[usuario_id - 1]
    return {'message': 'Usuário deletado'}


# PEDIDO
database_pedidos = []


@app.get('/pedidos/', response_model=PedidoLista)
def read_pedidos():
    return {'pedidos': database_pedidos}


@app.get('/pedidos/{pedido_id}', response_model=PedidoDB)
def read_pedido(pedido_id: int):
    if pedido_id > len(database_pedidos) or pedido_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )
    return database_pedidos[pedido_id - 1]


@app.post('/pedidos/', response_model=PedidoDB, status_code=HTTPStatus.CREATED)
def create_pedido(pedido: PedidoSchema):
    novo_pedido = PedidoDBData(
        id=len(database_pedidos) + 1,
        **pedido.model_dump(),
        cliente_id=len(database_pedidos) + 1,
        criado_em=datetime.now(),
    )
    database_pedidos.append(novo_pedido)
    return novo_pedido


@app.put('/pedidos/{pedido_id}', response_model=PedidoDB)
def update_pedido(pedido_id: int, pedido: PedidoSchema):
    if pedido_id > len(database_pedidos) or pedido_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )

    pedido_atualizado = PedidoDB(
        id=pedido_id,
        **pedido.model_dump(),
        cliente_id=1,
        criado_em=(database_pedidos[pedido_id - 1].criado_em),
    )
    database_pedidos[pedido_id - 1] = pedido_atualizado
    return pedido_atualizado


@app.delete('/pedidos/{pedido_id}', response_model=dict)
def delete_pedido(pedido_id: int):
    if pedido_id < 1 or pedido_id > len(database_pedidos):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )

    del database_pedidos[pedido_id - 1]
    return {'message': 'Pedido deletado'}


# PRODUTO
database_produtos = []


@app.get('/produtos/', response_model=ProdutoLista)
def read_produtos():
    return {'produtos': database_produtos}


@app.get('/produtos/{produto_id}', response_model=ProdutoDB)
def read_produto(produto_id: int):
    if produto_id > len(database_produtos) or produto_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )
    return database_produtos[produto_id - 1]


@app.post(
    '/produtos/', response_model=ProdutoDB, status_code=HTTPStatus.CREATED
)
def create_produto(produto: ProdutoSchema):
    novo_produto = ProdutoDB(
        id=len(database_produtos) + 1, **produto.model_dump()
    )
    database_produtos.append(novo_produto)
    return novo_produto


@app.put('/produtos/{produto_id}', response_model=ProdutoDB)
def update_produto(produto_id: int, produto: ProdutoSchema):
    if produto_id > len(database_produtos) or produto_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )

    produto_atualizado = ProdutoDB(id=produto_id, **produto.model_dump())
    database_produtos[produto_id - 1] = produto_atualizado
    return produto_atualizado


@app.delete('/produtos/{produto_id}', response_model=dict)
def delete_produto(produto_id: int):
    if produto_id < 1 or produto_id > len(database_produtos):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )

    del database_produtos[produto_id - 1]
    return {'message': 'Produto deletado'}
