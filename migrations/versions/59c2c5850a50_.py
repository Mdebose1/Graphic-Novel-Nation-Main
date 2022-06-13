"""empty message

Revision ID: 59c2c5850a50
Revises: 31cb33b10416
Create Date: 2022-06-07 15:47:54.630248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c2c5850a50'
down_revision = '31cb33b10416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'product_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
