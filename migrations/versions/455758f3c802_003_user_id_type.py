"""003_user_id_type

Revision ID: 455758f3c802
Revises: 723ed788711b
Create Date: 2019-02-04 13:28:27.227403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455758f3c802'
down_revision = '723ed788711b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE "user" DROP CONSTRAINT "user_pkey" CASCADE')
    op.alter_column('user', 'identity', existing_type=sa.Integer(), type_=sa.String())    
    op.create_primary_key('user_pkey', 'user', ['identity'])


def downgrade():
    op.execute('ALTER TABLE "user" DROP CONSTRAINT "user_pkey" CASCADE')    
    op.alter_column('user', 'identity', existing_type=sa.String(), type_=sa.Integer(), postgresql_using="identity::integer", autoincrement=True)
    op.create_primary_key('user_pkey', 'user', ['identity'])