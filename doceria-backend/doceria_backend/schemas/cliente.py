from datetime import date

from pydantic import BaseModel, EmailStr


class ClienteSchema(BaseModel):
    nome: str
    data_nascimento: date
    celular: str
    email: EmailStr


class ClienteDB(ClienteSchema):
    id: int


class ClienteLista(BaseModel):
    clientes: list[ClienteDB]
