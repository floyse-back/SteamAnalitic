"""Add many-to-many tables

Revision ID: b8235dae158b
Revises: 8005d2faa76d
Create Date: 2025-03-02 11:19:29.773953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8235dae158b'
down_revision: Union[str, None] = '8005d2faa76d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_to_many',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['game_id'], ['gamesdetails.steam_appid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('game_id', 'category_id')
    )
    op.create_unique_constraint(None, 'categories', ['category_name'])
    op.create_unique_constraint(None, 'ganres', ['ganres_name'])
    op.create_unique_constraint(None, 'publishers', ['publisher_name'])
    op.alter_column('steambase', 'appid',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('steambase', 'appid',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.drop_constraint(None, 'publishers', type_='unique')
    op.drop_constraint(None, 'ganres', type_='unique')
    op.drop_constraint(None, 'categories', type_='unique')
    op.drop_table('category_to_many')
    # ### end Alembic commands ###
