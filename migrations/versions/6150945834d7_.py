"""empty message

Revision ID: 6150945834d7
Revises: None
Create Date: 2017-01-18 14:09:11.482511

"""

# revision identifiers, used by Alembic.
revision = '6150945834d7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site_visits', sa.Column('throw_away_parameter', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site_visits', 'throw_away_parameter')
    ### end Alembic commands ###