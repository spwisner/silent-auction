"""add photos table

Revision ID: d0c32c1b0241
Revises: 36ec5861aaca
Create Date: 2024-01-10 17:54:31.203078

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'd0c32c1b0241'
down_revision = '36ec5861aaca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src', sa.String(length=75), nullable=False),
    sa.Column('caption', sa.String(length=100), nullable=True),
    sa.Column('category', sa.String(length=75), nullable=False),
    sa.Column('subcategory', sa.String(length=75), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False, default=datetime.utcnow),
    sa.Column('updated_at', sa.DateTime(), nullable=False, default=datetime.utcnow),
    sa.Column('auction_id', sa.Integer(), nullable=True),
    sa.Column('auction_item_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['auction_id'], ['auctions.id'], ),
    sa.ForeignKeyConstraint(['auction_item_id'], ['auction_items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photos')
    # ### end Alembic commands ###
