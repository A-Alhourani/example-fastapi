"""empty message

Revision ID: 956657c8bad1
Revises: 92a799019d33, c5b8ec555382
Create Date: 2023-10-25 04:27:39.664108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '956657c8bad1'
down_revision: Union[str, None] = ('92a799019d33', 'c5b8ec555382')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
