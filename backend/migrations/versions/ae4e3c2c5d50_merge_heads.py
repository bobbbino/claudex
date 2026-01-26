"""merge heads

Revision ID: ae4e3c2c5d50
Revises: e5f6g7h8i9j1, j0k1l2m3n4o5
Create Date: 2026-01-26 04:45:03.753697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae4e3c2c5d50'
down_revision: Union[str, None] = ('e5f6g7h8i9j1', 'j0k1l2m3n4o5')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
