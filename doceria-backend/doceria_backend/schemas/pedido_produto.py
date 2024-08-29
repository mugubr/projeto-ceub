from pydantic import BaseModel


class PedidoProdutoSchema(BaseModel):
    quantidade: float


class PedidoProdutoDB(BaseModel):
    id: int
    pedido_id: int
    produto_id: int
