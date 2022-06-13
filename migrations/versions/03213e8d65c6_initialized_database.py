"""Initialized Database

Revision ID: 03213e8d65c6
Revises: 
Create Date: 2022-06-05 16:34:54.925886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03213e8d65c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('post',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('author', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###
