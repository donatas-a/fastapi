"""create content column

Revision ID: 6517edd6d5d2
Revises: 7d584647d66f
Create Date: 2024-10-09 14:22:04.865585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6517edd6d5d2'
down_revision: Union[str, None] = '7d584647d66f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts","content")
