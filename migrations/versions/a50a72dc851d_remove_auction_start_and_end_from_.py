"""remove auction start and end from auction

Revision ID: a50a72dc851d
Revises: 53ee6ad0b8af
Create Date: 2024-01-09 19:30:48.411691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a50a72dc851d'
down_revision = '53ee6ad0b8af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.drop_column('auction_end')
        batch_op.drop_column('auction_start')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auctions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('auction_start', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('auction_end', sa.DATETIME(), nullable=False))

    # ### end Alembic commands ###
