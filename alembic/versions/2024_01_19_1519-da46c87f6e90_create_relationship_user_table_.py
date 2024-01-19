"""create relationship user table migrations

Revision ID: da46c87f6e90
Revises: 920a89d18721
Create Date: 2024-01-19 15:19:17.625862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da46c87f6e90'
down_revision: Union[str, None] = '920a89d18721'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('account_id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('qr_id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('gender_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'gender', ['gender_id'], ['id'])
    op.create_foreign_key(None, 'user', 'account', ['account_id'], ['id'])
    op.create_foreign_key(None, 'user', 'qr', ['qr_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'gender_id')
    op.drop_column('user', 'qr_id')
    op.drop_column('user', 'account_id')
    # ### end Alembic commands ###
    
