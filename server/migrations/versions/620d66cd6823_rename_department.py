"""rename department

Revision ID: 620d66cd6823
Revises: 0ba6f80b0a7b
Create Date: 2024-04-04 13:42:45.746506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '620d66cd6823'
down_revision = '0ba6f80b0a7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###