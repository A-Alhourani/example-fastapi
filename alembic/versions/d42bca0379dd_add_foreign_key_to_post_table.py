"""add foreign key to post table

Revision ID: d42bca0379dd
Revises: aa6386e68679
Create Date: 2023-10-25 03:54:39.623657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d42bca0379dd"
down_revision: Union[str, None] = "aa6386e68679"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None: 
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk','posts')
    op.drop_column('posts','owner_id')
    pass
