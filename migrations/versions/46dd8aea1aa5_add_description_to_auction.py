"""add description to auction

Revision ID: 46dd8aea1aa5
Revises: a50a72dc851d
Create Date: 2024-01-09 19:38:45.461980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46dd8aea1aa5'
down_revision = 'a50a72dc851d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=300), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###