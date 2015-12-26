"""init migration

Revision ID: 1a29f0653f1b
Revises: None
Create Date: 2015-12-26 17:23:10.420000

"""

# revision identifiers, used by Alembic.
revision = '1a29f0653f1b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activitys', sa.Column('passflag', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activitys', 'passflag')
    ### end Alembic commands ###
