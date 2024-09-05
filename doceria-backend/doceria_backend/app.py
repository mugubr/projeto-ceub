from datetime import datetime, timedelta
from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import extract, select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import (
    Cliente,
    Pedido,
    PedidoProduto,
    Produto,
    Usuario,
)
from doceria_backend.schemas.cliente import (
    ClienteCreateSchema,
    ClienteDB,
    ClienteLista,
    ClienteSchema,
)
from doceria_backend.schemas.pedido import (
    PedidoCreateSchema,
    PedidoDB,
    PedidoLista,
    PedidoPorMesResponseSchema,
    PedidoResponseSchema,
    PedidoSchema,
)
from doceria_backend.schemas.produto import (
    ProdutoCreateSchema,
    ProdutoDB,
    ProdutoLista,
    ProdutoSchema,
)
from doceria_backend.schemas.usuario import (
    UsuarioCreateSchema,
    UsuarioLista,
    UsuarioPublico,
    UsuarioSchema,
)
from doceria_backend.security import get_password_hash, verify_password

app = FastAPI(title='API Katherine Corrales - Doceria')


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo'}


@app.post('/token')
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    usuario = session.scalar(
        select(Usuario).where(Usuario.usuario == form_data.username)
    )

    if not usuario or not verify_password(form_data.password, usuario.senha):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Usuário ou senha incorretos',
        )
    ...


# CLIENTE
@app.get('/clientes/', response_model=ClienteLista)
def read_clientes(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    clientes = session.scalars(select(Cliente).limit(limit).offset(offset))
    return {'clientes': clientes}


@app.get('/clientes/{cliente_id}', response_model=ClienteDB)
def read_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente = session.scalar(select(Cliente).where(Cliente.id == cliente_id))
    if not cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )
    return cliente


@app.post(
    '/clientes/', response_model=ClienteDB, status_code=HTTPStatus.CREATED
)
def create_cliente(
    novo_cliente: ClienteCreateSchema, session: Session = Depends(get_session)
):
    cliente = session.scalar(
        select(Cliente).where(
            (Cliente.celular == novo_cliente.celular)
            | (Cliente.email == novo_cliente.email)
        )
    )

    if cliente:
        if cliente.celular == novo_cliente.celular:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Celular já cadastrado',
            )
        if cliente.email == novo_cliente.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='E-mail já cadastrado',
            )

    novo_cliente_db = Cliente(
        nome=novo_cliente.nome,
        data_nascimento=novo_cliente.data_nascimento,
        celular=novo_cliente.celular,
        email=novo_cliente.email,
    )

    session.add(novo_cliente_db)
    session.commit()
    session.refresh(novo_cliente_db)

    cliente_db = session.scalar(
        select(Cliente).where(
            (Cliente.celular == novo_cliente_db.celular)
            | (Cliente.email == novo_cliente_db.email)
        )
    )

    usuario_db = session.scalar(
        select(Usuario).where((Usuario.usuario == novo_cliente.usuario))
    )

    if usuario_db:
        if usuario_db.usuario == novo_cliente.usuario:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já cadastrado',
            )

    novo_usuario = Usuario(
        usuario=novo_cliente.usuario,
        senha=get_password_hash(novo_cliente.senha),
        cliente_id=cliente_db.id,
    )

    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)

    return novo_cliente_db


@app.put('/clientes/{cliente_id}', response_model=ClienteDB)
def update_cliente(
    cliente_id: int,
    cliente: ClienteSchema,
    session: Session = Depends(get_session),
):
    cliente_db = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )
    if not cliente_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )

    cliente_erro = session.scalar(
        select(Cliente).where(
            (Cliente.celular == cliente.celular)
            | (Cliente.email == cliente.email)
        )
    )

    if cliente_erro:
        if cliente_erro.celular == cliente.celular:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Celular já cadastrado',
            )
        if cliente_erro.email == cliente.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='E-mail já cadastrado',
            )

    cliente_db.nome = cliente.nome
    cliente_db.data_nascimento = cliente.data_nascimento
    cliente_db.celular = cliente.celular
    cliente_db.email = cliente.email

    session.commit()
    session.refresh(cliente_db)

    return cliente_db


@app.delete('/clientes/{cliente_id}', response_model=dict)
def delete_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente_db = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )
    if not cliente_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )
    session.delete(cliente_db)
    session.commit()
    return {'message': 'Cliente deletado'}


# USUARIO
@app.get('/usuarios/', response_model=UsuarioLista)
def read_usuarios(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    usuarios = session.scalars(select(Usuario).limit(limit).offset(offset))
    return {'usuarios': usuarios}


@app.get('/usuarios/{usuario_id}', response_model=UsuarioPublico)
def read_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.scalar(select(Usuario).where(Usuario.id == usuario_id))
    if not usuario:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    return usuario


@app.post(
    '/usuarios/', response_model=UsuarioPublico, status_code=HTTPStatus.CREATED
)
def create_usuario(
    novo_usuario: UsuarioCreateSchema, session: Session = Depends(get_session)
):
    usuario = session.scalar(
        select(Usuario).where(
            (Usuario.usuario == novo_usuario.usuario)
            | (Usuario.cliente_id == novo_usuario.cliente_id)
        )
    )

    if usuario:
        if usuario.usuario == novo_usuario.usuario:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já cadastrado',
            )
        if usuario.cliente_id == novo_usuario.cliente_id:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Cliente já cadastrado',
            )

    novo_usuario_db = Usuario(
        usuario=novo_usuario.usuario,
        senha=get_password_hash(novo_usuario.senha),
        cliente_id=novo_usuario.cliente_id,
    )

    session.add(novo_usuario_db)
    session.commit()
    session.refresh(novo_usuario_db)

    return novo_usuario_db


@app.put('/usuarios/{usuario_id}', response_model=UsuarioPublico)
def update_usuario(
    usuario_id: int,
    usuario: UsuarioSchema,
    session: Session = Depends(get_session),
):
    usuario_db = session.scalar(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    if not usuario_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    usuario_erro = session.scalar(
        select(Usuario).where((Usuario.usuario == usuario.usuario))
    )

    if usuario_erro:
        if usuario_erro.usuario == usuario.usuario:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já cadastrado',
            )

    usuario_db.usuario = usuario.usuario
    usuario_db.senha = usuario.senha

    session.commit()
    session.refresh(usuario_db)

    return usuario_db


@app.delete('/usuarios/{usuario_id}', response_model=dict)
def delete_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario_db = session.scalar(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    if not usuario_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    session.delete(usuario_db)
    session.commit()
    return {'message': 'Usuário deletado'}


# PEDIDO
@app.get('/pedidos/', response_model=PedidoLista)
def read_pedidos(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    pedidos = session.scalars(select(Pedido).limit(limit).offset(offset)).all()

    resposta = []

    for pedido in pedidos:
        pedido_produtos = session.scalars(
            select(PedidoProduto).where(PedidoProduto.pedido_id == pedido.id)
        ).all()

        valor_total = 0.0
        for pedido_produto in pedido_produtos:
            produto = session.scalar(
                select(Produto).where(Produto.id == pedido_produto.produto_id)
            )

            valor_total += produto.preco * pedido_produto.quantidade

        status = 'Em andamento'
        hoje = datetime.now().date()
        if pedido.data_entrega < hoje:
            status = 'Entregue'

        celular = ''
        cliente = session.scalar(
            select(Cliente).where(Cliente.id == pedido.cliente_id)
        )
        if cliente.celular:
            celular = cliente.celular

        descricao = ''
        for pedido_produto in pedido_produtos:
            produto = session.scalar(
                select(Produto).where(Produto.id == pedido_produto.produto_id)
            )
            descricao += f'{str(int(pedido_produto.quantidade))}X {
                produto.nome
            }, '

        pedido_resposta = PedidoResponseSchema(
            id=pedido.id,
            cliente_id=pedido.cliente_id,
            criado_em=pedido.criado_em,
            data_entrega=pedido.data_entrega,
            ocasiao=pedido.ocasiao,
            bairro=pedido.bairro,
            logradouro=pedido.logradouro,
            numero_complemento=pedido.numero_complemento,
            ponto_referencia=pedido.ponto_referencia,
            valor=valor_total,
            status=status,
            celular=celular,
            descricao=descricao.rstrip(', '),
        )
        resposta.append(pedido_resposta)

    return {'pedidos': resposta}


@app.get('/pedidos/cliente/{cliente_id}', response_model=PedidoLista)
def read_pedidos_by_cliente(
    cliente_id: int, session: Session = Depends(get_session)
):
    pedidos = session.scalars(
        select(Pedido).where(Pedido.cliente_id == cliente_id)
    ).all()

    resposta = []

    for pedido in pedidos:
        pedido_produtos = session.scalars(
            select(PedidoProduto).where(PedidoProduto.pedido_id == pedido.id)
        ).all()

        valor_total = 0.0
        for pedido_produto in pedido_produtos:
            produto = session.scalar(
                select(Produto).where(Produto.id == pedido_produto.produto_id)
            )

            valor_total += produto.preco * pedido_produto.quantidade

        status = 'Em andamento'
        hoje = datetime.now().date()
        if pedido.data_entrega < hoje:
            status = 'Entregue'

        celular = ''
        cliente = session.scalar(
            select(Cliente).where(Cliente.id == pedido.cliente_id)
        )
        if cliente.celular:
            celular = cliente.celular

        descricao = ''
        for pedido_produto in pedido_produtos:
            produto = session.scalar(
                select(Produto).where(Produto.id == pedido_produto.produto_id)
            )
            descricao += f'{str(int(pedido_produto.quantidade))}X {
                produto.nome
            }, '

        pedido_resposta = PedidoResponseSchema(
            id=pedido.id,
            cliente_id=pedido.cliente_id,
            criado_em=pedido.criado_em,
            data_entrega=pedido.data_entrega,
            ocasiao=pedido.ocasiao,
            bairro=pedido.bairro,
            logradouro=pedido.logradouro,
            numero_complemento=pedido.numero_complemento,
            ponto_referencia=pedido.ponto_referencia,
            valor=valor_total,
            status=status,
            celular=celular,
            descricao=descricao.rstrip(', '),
        )
        resposta.append(pedido_resposta)

    return {'pedidos': resposta}


@app.get('/pedidos/mes/{mes}', response_model=PedidoPorMesResponseSchema)
def read_pedidos_by_mes(
    ano: int,
    mes: int,
    session: Session = Depends(get_session),
):
    pedidos = session.scalars(
        select(Pedido)
        .where(
            extract('year', Pedido.criado_em) == ano,
            extract('month', Pedido.criado_em) == mes,
        )
        .order_by(Pedido.criado_em)
    ).all()

    if not pedidos:
        raise HTTPException(status_code=404, detail='Nenhum pedido encontrado')

    pedidos_agrupados = {}

    for pedido in pedidos:
        pedido_produtos = session.scalars(
            select(PedidoProduto).where(PedidoProduto.pedido_id == pedido.id)
        ).all()

        valor_total = 0.0
        descricao = ''
        for pedido_produto in pedido_produtos:
            produto = session.scalar(
                select(Produto).where(Produto.id == pedido_produto.produto_id)
            )
            valor_total += produto.preco * pedido_produto.quantidade
            descricao += f'{int(pedido_produto.quantidade)}X {produto.nome}, '

        status = 'Em andamento'
        hoje = datetime.now().date()
        if pedido.data_entrega and pedido.data_entrega < hoje:
            status = 'Entregue'

        celular = ''
        cliente = session.scalar(
            select(Cliente).where(Cliente.id == pedido.cliente_id)
        )
        if cliente and cliente.celular:
            celular = cliente.celular

        pedido_resposta = PedidoResponseSchema(
            id=pedido.id,
            cliente_id=pedido.cliente_id,
            criado_em=pedido.criado_em,
            data_entrega=pedido.data_entrega,
            ocasiao=pedido.ocasiao,
            bairro=pedido.bairro,
            logradouro=pedido.logradouro,
            numero_complemento=pedido.numero_complemento,
            ponto_referencia=pedido.ponto_referencia,
            valor=valor_total,
            status=status,
            celular=celular,
            descricao=descricao.rstrip(', '),
        )

        dia = pedido.criado_em.day
        if dia not in pedidos_agrupados:
            pedidos_agrupados[dia] = []
        pedidos_agrupados[dia].append(pedido_resposta)

    return {'ano': ano, 'mes': mes, 'pedidos': pedidos_agrupados}


@app.get('/pedidos/{pedido_id}', response_model=PedidoResponseSchema)
def read_pedido(pedido_id: int, session: Session = Depends(get_session)):
    pedido = session.scalar(select(Pedido).where(Pedido.id == pedido_id))
    if not pedido:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )

    pedido_produtos = session.scalars(
        select(PedidoProduto).where(PedidoProduto.pedido_id == pedido.id)
    ).all()

    valor_total = 0.0
    for pedido_produto in pedido_produtos:
        produto = session.scalar(
            select(Produto).where(Produto.id == pedido_produto.produto_id)
        )

        valor_total += produto.preco * pedido_produto.quantidade

    status = 'Em andamento'
    hoje = datetime.now().date()
    if pedido.data_entrega < hoje:
        status = 'Entregue'

    celular = ''
    cliente = session.scalar(
        select(Cliente).where(Cliente.id == pedido.cliente_id)
    )
    if cliente.celular:
        celular = cliente.celular

    descricao = ''
    for pedido_produto in pedido_produtos:
        produto = session.scalar(
            select(Produto).where(Produto.id == pedido_produto.produto_id)
        )
        descricao += f'{str(int(pedido_produto.quantidade))}X {produto.nome}, '

    pedido_resposta = PedidoResponseSchema(
        id=pedido.id,
        cliente_id=pedido.cliente_id,
        criado_em=pedido.criado_em,
        data_entrega=pedido.data_entrega,
        ocasiao=pedido.ocasiao,
        bairro=pedido.bairro,
        logradouro=pedido.logradouro,
        numero_complemento=pedido.numero_complemento,
        ponto_referencia=pedido.ponto_referencia,
        valor=valor_total,
        status=status,
        celular=celular,
        descricao=descricao.rstrip(', '),
    )
    return pedido_resposta


@app.post(
    '/pedidos/',
    response_model=PedidoDB,
    status_code=HTTPStatus.CREATED,
)
def create_pedido(
    novo_pedido: PedidoCreateSchema, session: Session = Depends(get_session)
):
    hoje = datetime.now().date()
    uma_semana = hoje + timedelta(days=3)

    pedido_minimo_por_produto = 25

    if (hoje > novo_pedido.data_entrega) | (
        hoje <= novo_pedido.data_entrega <= uma_semana
    ):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Insira uma data válida.',
        )

    novo_pedido_db = Pedido(
        data_entrega=novo_pedido.data_entrega,
        ocasiao=novo_pedido.ocasiao,
        bairro=novo_pedido.bairro,
        logradouro=novo_pedido.logradouro,
        numero_complemento=novo_pedido.numero_complemento,
        ponto_referencia=novo_pedido.ponto_referencia,
        cliente_id=novo_pedido.cliente_id,
    )

    session.add(novo_pedido_db)
    session.commit()
    session.refresh(novo_pedido_db)

    pedido_db = session.scalar(
        select(Pedido).where((Pedido.cliente_id == novo_pedido.cliente_id))
    )

    for produto in novo_pedido.produtos:
        if produto.quantidade < pedido_minimo_por_produto:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='O pedido mínimo, por produto, é de 25 unidades',
            )

        novo_pedido_produto = PedidoProduto(
            pedido_id=pedido_db.id,
            produto_id=produto.produto_id,
            quantidade=produto.quantidade,
        )

        session.add(novo_pedido_produto)
        session.commit()
        session.refresh(novo_pedido_produto)

    return novo_pedido_db


@app.put('/pedidos/{pedido_id}', response_model=PedidoDB)
def update_pedido(
    pedido_id: int,
    pedido: PedidoSchema,
    session: Session = Depends(get_session),
):
    pedido_db = session.scalar(select(Pedido).where(Pedido.id == pedido_id))
    if not pedido_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )

    pedido_db.data_entrega = pedido.data_entrega
    pedido_db.ocasiao = pedido.ocasiao
    pedido_db.bairro = pedido.bairro
    pedido_db.logradouro = pedido.logradouro
    pedido_db.numero_complemento = pedido.numero_complemento
    pedido_db.ponto_referencia = pedido.ponto_referencia

    session.commit()
    session.refresh(pedido_db)

    return pedido_db


@app.delete('/pedidos/{pedido_id}', response_model=dict)
def delete_pedido(pedido_id: int, session: Session = Depends(get_session)):
    pedido_db = session.scalar(select(Pedido).where(Pedido.id == pedido_id))
    if not pedido_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )
    session.delete(pedido_db)
    session.commit()
    return {'message': 'Pedido deletado'}


# PRODUTO
@app.get('/produtos/', response_model=ProdutoLista)
def read_produtos(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    produtos = session.scalars(select(Produto).limit(limit).offset(offset))
    return {'produtos': produtos}


@app.get('/produtos/{produto_id}', response_model=ProdutoDB)
def read_produto(produto_id: int, session: Session = Depends(get_session)):
    produto = session.scalar(select(Produto).where(Produto.id == produto_id))
    if not produto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )
    return produto


@app.post(
    '/produtos/', response_model=ProdutoDB, status_code=HTTPStatus.CREATED
)
def create_produto(
    novo_produto: ProdutoCreateSchema, session: Session = Depends(get_session)
):
    produto = session.scalar(
        select(Produto).where((Produto.nome == novo_produto.nome))
    )

    if produto:
        if produto.nome == novo_produto.nome:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Produto já cadastrado',
            )

    novo_produto_db = Produto(
        nome=novo_produto.nome,
        preco=novo_produto.preco,
        tempo_producao=novo_produto.tempo_producao,
        vegano=novo_produto.vegano,
        gluten=novo_produto.gluten,
        lactose=novo_produto.lactose,
    )

    session.add(novo_produto_db)
    session.commit()
    session.refresh(novo_produto_db)

    return novo_produto_db


@app.put('/produtos/{produto_id}', response_model=ProdutoDB)
def update_produto(
    produto_id: int,
    produto: ProdutoSchema,
    session: Session = Depends(get_session),
):
    produto_db = session.scalar(
        select(Produto).where(Produto.id == produto_id)
    )
    if not produto_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.tempo_producao = produto.tempo_producao
    produto_db.vegano = produto.vegano
    produto_db.gluten = produto.gluten
    produto_db.lactose = produto.lactose

    session.commit()
    session.refresh(produto_db)

    return produto_db


@app.delete('/produtos/{produto_id}', response_model=dict)
def delete_produto(produto_id: int, session: Session = Depends(get_session)):
    produto_db = session.scalar(
        select(Produto).where(Produto.id == produto_id)
    )
    if not produto_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )
    session.delete(produto_db)
    session.commit()
    return {'message': 'Produto deletado'}
