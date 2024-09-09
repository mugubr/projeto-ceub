from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from doceria_backend.database import get_session
from doceria_backend.models import Produto
from doceria_backend.schemas.produto import (
    ProdutoCreateSchema,
    ProdutoDB,
    ProdutoLista,
    ProdutoSchema,
)
from doceria_backend.security import get_admin, get_current_user

router = APIRouter(prefix='/produtos', tags=['Produtos'])


@router.get('/', response_model=ProdutoLista)
def read_produtos(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    produtos = session.scalars(select(Produto).limit(limit).offset(offset))
    return {'produtos': produtos}


@router.get('/{produto_id}', response_model=ProdutoDB)
def read_produto(
    produto_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    produto = session.scalar(select(Produto).where(Produto.id == produto_id))
    if not produto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )
    return produto


@router.post('/', response_model=ProdutoDB, status_code=HTTPStatus.CREATED)
def create_produto(
    novo_produto: ProdutoCreateSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
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


@router.put('/{produto_id}', response_model=ProdutoDB)
def update_produto(
    produto_id: int,
    produto: ProdutoSchema,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
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


@router.delete('/{produto_id}', response_model=dict)
def delete_produto(
    produto_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_admin),
):
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
