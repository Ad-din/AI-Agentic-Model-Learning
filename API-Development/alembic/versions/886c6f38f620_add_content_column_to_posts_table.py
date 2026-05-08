"""add content column to posts table

Revision ID: 886c6f38f620
Revises: 91bea3317a6f
Create Date: 2026-05-06 06:12:19.927650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '886c6f38f620'
down_revision: Union[str, Sequence[str], None] = '91bea3317a6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False,))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')

    pass
