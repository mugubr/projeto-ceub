from datetime import date

from pydantic import BaseModel, EmailStr


class ClienteSchema(BaseModel):
    nome: str
    data_nascimento: date
    celular: str
    email: EmailStr


class ClienteCreateSchema(ClienteSchema):
    usuario: str
    senha: str


class ClienteDB(ClienteSchema):
    id: int


class ClienteLista(BaseModel):
    clientes: list[ClienteDB]
