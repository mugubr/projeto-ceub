from pydantic import BaseModel


class MensagemSchema(BaseModel):
    id: int
    mensagem: str


class MensagemCreateSchema(BaseModel):
    mensagem: str


class MensagemUpdateSchema(MensagemCreateSchema): ...


class MensagemLista(BaseModel):
    mensagens: list[MensagemSchema]
