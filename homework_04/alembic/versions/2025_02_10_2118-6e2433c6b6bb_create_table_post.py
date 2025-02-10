"""create table Post

Revision ID: 6e2433c6b6bb
Revises: d3c145b2fcd7
Create Date: 2025-02-10 21:18:24.701257

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "6e2433c6b6bb"
down_revision: Union[str, None] = "d3c145b2fcd7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "title",
            sa.String(length=400),
            server_default="Brave New Post",
            nullable=False,
        ),
        sa.Column("body", sa.Text(), server_default="", nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("fk_post_user_id_user")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_post")),
    )


def downgrade() -> None:
    op.drop_table("post")
