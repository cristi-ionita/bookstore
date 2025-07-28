from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "b51412ac4808"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("author", sa.String(length=100), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
    )
    op.create_index("ix_users_username", "users", ["username"], unique=True)
    op.create_index("ix_users_email", "users", ["email"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    op.drop_table("books")
