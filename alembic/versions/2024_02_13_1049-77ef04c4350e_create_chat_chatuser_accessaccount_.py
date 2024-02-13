""" create chat, chatuser, accessaccount, doctor tables

Revision ID: 77ef04c4350e
Revises: bb165ca448b9
Create Date: 2024-02-13 10:49:55.567924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77ef04c4350e'
down_revision: Union[str, None] = 'bb165ca448b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('previous_chat_id', sa.Integer(), nullable=False),
    sa.Column('speciality_id', sa.Integer(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], name='chat_account_fk', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['previous_chat_id'], ['chat.id'], name='previous_chat_id', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['speciality_id'], ['speciality.id'], name='chat_speciality_fk', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('previous_chat_id')
    )
    op.create_index(op.f('ix_chat_active'), 'chat', ['active'], unique=False)
    op.create_table('doctor',
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('creater_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('speciality_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], name='doctor_account_fk', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['creater_id'], ['account.id'], name='doctor_creater_id', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['speciality_id'], ['speciality.id'], name='doctor_speciality_fk', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id'),
    sa.UniqueConstraint('account_id', 'speciality_id', name='account_speciality_uc')
    )
    op.create_index(op.f('ix_doctor_is_active'), 'doctor', ['is_active'], unique=False)
    op.create_table('chatuser',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='chatuser_user_fk', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chatuser')
    op.drop_index(op.f('ix_doctor_is_active'), table_name='doctor')
    op.drop_table('doctor')
    op.drop_index(op.f('ix_chat_active'), table_name='chat')
    op.drop_table('chat')
    # ### end Alembic commands ###
