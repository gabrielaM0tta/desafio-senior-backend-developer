"""create transport_pass table

Revision ID: a9b176598c4b
Revises: 29036f8ff879
Create Date: 2025-05-10 18:50:23.896887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9b176598c4b'
down_revision: Union[str, None] = '29036f8ff879'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transport_pass',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('saldo', sa.Float(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transport_pass_id'), 'transport_pass', ['id'], unique=False)
    op.create_index(op.f('ix_transport_pass_username'), 'transport_pass', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transport_pass_username'), table_name='transport_pass')
    op.drop_index(op.f('ix_transport_pass_id'), table_name='transport_pass')
    op.drop_table('transport_pass')
    # ### end Alembic commands ###
