from datetime import date, datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Mensagem:
    __tablename__ = 'mensagens'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    mensagem: Mapped[str]


@table_registry.mapped_as_dataclass
class Cliente:
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    data_nascimento: Mapped[date]
    celular: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    criado_em: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now()
    )
    usuario: Mapped['Usuario'] = relationship(
        init=False, back_populates='cliente'
    )

    pedidos: Mapped[list['Pedido']] = relationship(
        init=False, back_populates='cliente', cascade='all, delete-orphan'
    )


@table_registry.mapped_as_dataclass
class Usuario:
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    usuario: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]

    cliente_id: Mapped[int] = mapped_column(ForeignKey('clientes.id'))

    cliente: Mapped[Cliente] = relationship(
        init=False, back_populates='usuario'
    )


@table_registry.mapped_as_dataclass
class Pedido:
    __tablename__ = 'pedidos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    data_entrega: Mapped[date]
    ocasiao: Mapped[str]
    bairro: Mapped[str]
    logradouro: Mapped[str]
    numero_complemento: Mapped[str]
    ponto_referencia: Mapped[str]
    criado_em: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    cliente_id: Mapped[int] = mapped_column(ForeignKey('clientes.id'))

    cliente: Mapped[Cliente] = relationship(
        init=False, back_populates='pedidos'
    )


@table_registry.mapped_as_dataclass
class Produto:
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    preco: Mapped[float]
    tempo_producao: Mapped[int]
    vegano: Mapped[bool]
    gluten: Mapped[bool]
    lactose: Mapped[bool]


@table_registry.mapped_as_dataclass
class PedidoProduto:
    __tablename__ = 'pedidos_produtos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    quantidade: Mapped[float]

    pedido_id: Mapped[int] = mapped_column(ForeignKey('pedidos.id'))

    pedido: Mapped[Pedido] = relationship(
        init=False, back_populates='pedidos_produtos'
    )

    produto_id: Mapped[int] = mapped_column(ForeignKey('produtos.id'))

    produto: Mapped[Produto] = relationship(
        init=False, back_populates='pedidos_produtos'
    )
