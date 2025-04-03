"""empty message

Revision ID: 8215c2ef31c9
Revises: 5cbb58a258d4
Create Date: 2025-04-02 21:08:21.246273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8215c2ef31c9'
down_revision: Union[str, None] = '5cbb58a258d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=True),
    sa.Column('reason', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blacklist_id'), 'blacklist', ['id'], unique=False)
    op.create_index(op.f('ix_blacklist_token'), 'blacklist', ['token'], unique=False)
    op.alter_column('refreshtokens', 'delete_time',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('refreshtokens', 'delete_time',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.drop_index(op.f('ix_blacklist_token'), table_name='blacklist')
    op.drop_index(op.f('ix_blacklist_id'), table_name='blacklist')
    op.drop_table('blacklist')
    # ### end Alembic commands ###
