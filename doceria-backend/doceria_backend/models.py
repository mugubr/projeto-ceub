from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Usuario:
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    cliente_id: Mapped[int] = mapped_column(unique=True)
    usuario: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]
