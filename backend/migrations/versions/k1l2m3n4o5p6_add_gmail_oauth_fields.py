"""add gmail oauth fields

Revision ID: k1l2m3n4o5p6
Revises: j0k1l2m3n4o5
Create Date: 2026-01-26 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'k1l2m3n4o5p6'
down_revision: Union[str, None] = 'j0k1l2m3n4o5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [c['name'] for c in inspector.get_columns('user_settings')]

    # Use Text for encrypted fields - EncryptedJSON stores encrypted strings, not JSON
    if 'gmail_oauth_client' not in columns:
        op.add_column('user_settings', sa.Column('gmail_oauth_client', sa.Text(), nullable=True))

    if 'gmail_oauth_tokens' not in columns:
        op.add_column('user_settings', sa.Column('gmail_oauth_tokens', sa.Text(), nullable=True))

    if 'gmail_connected_at' not in columns:
        op.add_column('user_settings', sa.Column('gmail_connected_at', sa.DateTime(), nullable=True))

    if 'gmail_email' not in columns:
        op.add_column('user_settings', sa.Column('gmail_email', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('user_settings', 'gmail_email')
    op.drop_column('user_settings', 'gmail_connected_at')
    op.drop_column('user_settings', 'gmail_oauth_tokens')
    op.drop_column('user_settings', 'gmail_oauth_client')
