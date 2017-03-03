"""empty message

Revision ID: 70415e1d7c03
Revises: 
Create Date: 2017-03-03 12:36:48.666455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70415e1d7c03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('email_id', sa.String(length=60), nullable=False),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('gender', sa.Binary(), nullable=True),
    sa.Column('oauth_id', sa.String(length=256), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('confirmation_status', sa.Boolean(), nullable=True),
    sa.Column('x_auth_token', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('oauth_id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('x_auth_token')
    )
    op.create_index(op.f('ix_user_email_id'), 'user', ['email_id'], unique=True)
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.drop_index(op.f('ix_user_email_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###