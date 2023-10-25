"""add content

Revision ID: e33b2fc451c7
Revises: b23daa4d00c9
Create Date: 2023-10-25 03:38:38.130897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e33b2fc451c7'
down_revision: Union[str, None] = 'b23daa4d00c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts',"content")
    pass
