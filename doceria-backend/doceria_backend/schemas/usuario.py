from pydantic import BaseModel


class UsuarioSchema(BaseModel):
    usuario: str
    senha: str


class UsuarioDB(UsuarioSchema):
    id: int
    cliente_id: int


class UsuarioPublico(BaseModel):
    id: int
    usuario: str


class UsuarioLista(BaseModel):
    usuarios: list[UsuarioPublico]
