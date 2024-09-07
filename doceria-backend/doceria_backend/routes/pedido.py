from datetime import datetime, timedelta
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import extract, select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import Cliente, Pedido, PedidoProduto, Produto
from doceria_backend.schemas.pedido import (
    PedidoCreateSchema,
    PedidoDB,
    PedidoLista,
    PedidoPorMesResponseSchema,
    PedidoResponseSchema,
    PedidoSchema,
)
from doceria_backend.security import get_admin, get_current_user

router = APIRouter(prefix='/pedidos', tags=['Pedidos'])


@router.get('/', response_model=PedidoLista)
def read_pedidos(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
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


@router.get('/cliente/{cliente_id}', response_model=PedidoLista)
def read_pedidos_by_cliente(
    cliente_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    cliente_id = current_user.cliente_id
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


@router.get('/mes/{mes}', response_model=PedidoPorMesResponseSchema)
def read_pedidos_by_mes(
    ano: int,
    mes: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
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


@router.get('/{pedido_id}', response_model=PedidoResponseSchema)
def read_pedido(
    pedido_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
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


@router.post(
    '/',
    response_model=PedidoDB,
    status_code=HTTPStatus.CREATED,
)
def create_pedido(
    novo_pedido: PedidoCreateSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    if current_user.cliente_id != novo_pedido.cliente_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Acesso negado'
        )
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


@router.put('/{pedido_id}', response_model=PedidoDB)
def update_pedido(
    pedido_id: int,
    pedido: PedidoSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    pedido_db = session.scalar(select(Pedido).where(Pedido.id == pedido_id))
    if not pedido_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )

    if current_user.cliente_id != pedido_db.cliente_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Acesso negado'
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


@router.delete('/{pedido_id}', response_model=dict)
def delete_pedido(
    pedido_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    pedido_db = session.scalar(select(Pedido).where(Pedido.id == pedido_id))
    if not pedido_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Pedido não encontrado'
        )
    if current_user.cliente_id != pedido_db.cliente_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Acesso negado'
        )
    session.delete(pedido_db)
    session.commit()
    return {'message': 'Pedido deletado'}
