"""Initial Migration

Revision ID: bc38ef47ec13
Revises:
Create Date: 2021-04-16 16:55:53.587323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bc38ef47ec13"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(20), nullable=False),
        sa.Column("last_name", sa.String(20), nullable=False),
        sa.Column("email", sa.String(120), unique=True, nullable=False),
    )

    op.create_table(
        "account",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(80), unique=True, nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id"), nullable=False),
        sa.Column("password_hash", sa.String(128)),
    )

    op.create_table(
        "transaction",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "account_id", sa.Integer, sa.ForeignKey("account.id"), nullable=False
        ),
        sa.Column("operation", sa.String(20), nullable=False),
        sa.Column("value", sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table("transaction")
    op.drop_table("account")
    op.drop_table("user")
