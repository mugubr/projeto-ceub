from datetime import date, datetime

from pydantic import BaseModel


class PedidoSchema(BaseModel):
    data_entrega: date
    ocasiao: str
    bairro: str
    logradouro: str
    numero_complemento: str
    ponto_referencia: str


class PedidoDB(PedidoSchema):
    id: int
    cliente_id: int


class PedidoDBData(PedidoDB):
    criado_em: datetime


class PedidoLista(BaseModel):
    pedidos: list[PedidoDB]
