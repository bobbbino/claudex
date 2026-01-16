"""add e2b fields back

Revision ID: g7h8i9j0k1l2
Revises: f6g7h8i9j0k1
Create Date: 2026-01-14 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'g7h8i9j0k1l2'
down_revision: Union[str, None] = 'f6g7h8i9j0k1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)

    user_settings_columns = [c['name'] for c in inspector.get_columns('user_settings')]
    chats_columns = [c['name'] for c in inspector.get_columns('chats')]

    if 'e2b_api_key' not in user_settings_columns:
        op.add_column('user_settings', sa.Column('e2b_api_key', sa.String(), nullable=True))

    if 'sandbox_provider' not in user_settings_columns:
        op.add_column('user_settings', sa.Column('sandbox_provider', sa.String(length=20), server_default='docker', nullable=False))
    else:
        op.execute("UPDATE user_settings SET sandbox_provider = 'docker' WHERE sandbox_provider IS NULL")

    if 'sandbox_provider' not in chats_columns:
        op.add_column('chats', sa.Column('sandbox_provider', sa.String(length=20), nullable=True))


def downgrade() -> None:
    op.drop_column('chats', 'sandbox_provider')
    op.drop_column('user_settings', 'sandbox_provider')
    op.drop_column('user_settings', 'e2b_api_key')
