from datetime import date, datetime

from pydantic import BaseModel

from doceria_backend.schemas.pedido_produto import PedidoProdutoCreateSchema


class PedidoSchema(BaseModel):
    data_entrega: date
    ocasiao: str
    bairro: str
    logradouro: str
    numero_complemento: str
    ponto_referencia: str


class PedidoCreateSchema(PedidoSchema):
    cliente_id: int
    produtos: list[PedidoProdutoCreateSchema]


class PedidoDB(PedidoSchema):
    id: int
    cliente_id: int


class PedidoDBData(PedidoSchema):
    criado_em: datetime


class PedidoResponseSchema(PedidoDB):
    valor: float
    status: str
    celular: str
    descricao: str
    nome: str


class PedidoResponseDataSchema(PedidoResponseSchema):
    criado_em: datetime


class PedidoPorMesResponseSchema(BaseModel):
    ano: int
    mes: int
    pedidos: dict[int, list[PedidoResponseSchema]]


class PedidoLista(BaseModel):
    pedidos: list[PedidoResponseDataSchema]
