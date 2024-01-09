"""add createdat and updatedat to user

Revision ID: 42dfa70b9bc9
Revises: 87029b211ff5
Create Date: 2024-01-09 21:01:42.460060

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '42dfa70b9bc9'
down_revision = '87029b211ff5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False, default=datetime.utcnow))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=False, default=datetime.utcnow))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
