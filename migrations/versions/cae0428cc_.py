"""empty message

Revision ID: cae0428cc
Revises: 55cfad75c353
Create Date: 2016-11-01 16:59:17.740772

"""

# revision identifiers, used by Alembic.
revision = 'cae0428cc'
down_revision = '55cfad75c353'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    ### end Alembic commands ###