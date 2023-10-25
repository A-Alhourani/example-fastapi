"""empty message

Revision ID: 92a799019d33
Revises: aa6386e68679
Create Date: 2023-10-25 03:53:32.523633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92a799019d33'
down_revision: Union[str, None] = 'aa6386e68679'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
