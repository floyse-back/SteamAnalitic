"""Add Column final_formatted_price

Revision ID: 980608495897
Revises: db4a344f911e
Create Date: 2025-03-02 14:03:24.100474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '980608495897'
down_revision: Union[str, None] = 'db4a344f911e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gamesdetails', sa.Column('final_formatted_price', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gamesdetails', 'final_formatted_price')
    # ### end Alembic commands ###
