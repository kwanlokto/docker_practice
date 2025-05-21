"""add created_at

Revision ID: 66e2e2850c0b
Revises: bc38ef47ec13
Create Date: 2025-05-21 01:43:25.274195

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '66e2e2850c0b'
down_revision = 'bc38ef47ec13'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('transaction', sa.Column(
        'created_at', sa.DateTime, default=datetime.datetime.utcnow, server_default=sa.func.now())
    )


def downgrade():
    op.drop_column('transaction', 'created_at')