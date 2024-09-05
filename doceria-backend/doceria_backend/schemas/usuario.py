from pydantic import BaseModel


class UsuarioSchema(BaseModel):
    usuario: str
    senha: str


class UsuarioCreateSchema(UsuarioSchema):
    cliente_id: int


class UsuarioDB(UsuarioSchema):
    id: int
    cliente_id: int


class UsuarioPublico(BaseModel):
    id: int
    usuario: str
    cliente_id: int


class UsuarioLista(BaseModel):
    usuarios: list[UsuarioPublico]
