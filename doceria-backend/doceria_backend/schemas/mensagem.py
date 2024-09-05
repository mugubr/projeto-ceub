from pydantic import BaseModel


class Mesagem(BaseModel):
    id: int
    mensagem: str
