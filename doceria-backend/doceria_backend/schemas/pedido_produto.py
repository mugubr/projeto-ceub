from pydantic import BaseModel


class PedidoProdutoSchema(BaseModel):
    quantidade: float


class PedidoProdutoCreateSchema(PedidoProdutoSchema):
    produto_id: int


class PedidoProdutoDB(BaseModel):
    id: int
    pedido_id: int
    produto_id: int
