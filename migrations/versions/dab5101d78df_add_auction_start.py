"""Add auction start

Revision ID: dab5101d78df
Revises: e70c72fc7e14
Create Date: 2024-01-09 17:50:34.523079

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dab5101d78df'
down_revision = 'e70c72fc7e14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('auction_start', sa.DateTime(), nullable=False, default=datetime.utcnow))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False, default=datetime.utcnow))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=False, default=datetime.utcnow))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('auction_start')

    # ### end Alembic commands ###