"""empty message

Revision ID: 6f4936eb9c80
Revises: 8a0e5a62259a
Create Date: 2025-03-22 11:19:19.209632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f4936eb9c80'
down_revision: Union[str, None] = '8a0e5a62259a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('refreshtokens', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'refreshtokens', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'refreshtokens', type_='foreignkey')
    op.drop_column('refreshtokens', 'user_id')
    # ### end Alembic commands ###
