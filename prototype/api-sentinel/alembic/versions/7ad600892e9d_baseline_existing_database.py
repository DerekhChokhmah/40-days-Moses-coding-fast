"""baseline existing database

Revision ID: 7ad600892e9d
Revises:
Create Date: 2026-11-02 17:58:02.584357
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7ad600892e9d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass