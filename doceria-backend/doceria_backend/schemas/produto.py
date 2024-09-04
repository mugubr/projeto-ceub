from pydantic import BaseModel


class ProdutoSchema(BaseModel):
    nome: str
    preco: float
    tempo_producao: int
    vegano: bool
    gluten: bool
    lactose: bool


class ProdutoCreateSchema(ProdutoSchema): ...


class ProdutoDB(ProdutoSchema):
    id: int


class ProdutoLista(BaseModel):
    produtos: list[ProdutoDB]
