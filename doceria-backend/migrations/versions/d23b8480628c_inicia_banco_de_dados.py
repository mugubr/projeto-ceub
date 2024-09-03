"""inicia banco de dados

Revision ID: d23b8480628c
Revises: 
Create Date: 2024-09-03 11:14:46.475224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd23b8480628c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('usuario', sa.String(), nullable=False),
    sa.Column('senha', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cliente_id'),
    sa.UniqueConstraint('usuario')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
