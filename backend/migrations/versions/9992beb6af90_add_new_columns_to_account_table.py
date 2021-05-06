"""add new columns to account table

Revision ID: 9992beb6af90
Revises: bc38ef47ec13
Create Date: 2021-05-05 21:38:21.254222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9992beb6af90"
down_revision = "bc38ef47ec13"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("account", sa.Column("access_token", sa.String(10)))


def downgrade():
    op.drop_column("account", "access_token")
