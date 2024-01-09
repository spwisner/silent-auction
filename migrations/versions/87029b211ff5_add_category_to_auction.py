"""add category to auction

Revision ID: 87029b211ff5
Revises: 46dd8aea1aa5
Create Date: 2024-01-09 19:58:58.311578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87029b211ff5'
down_revision = '46dd8aea1aa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.drop_column('category')

    # ### end Alembic commands ###