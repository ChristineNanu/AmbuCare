"""Increase phone column length

Revision ID: 993007ca8861
Revises: 553ee3772c65
Create Date: 2025-01-13 13:11:17.860169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '993007ca8861'
down_revision = '553ee3772c65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=15),
               existing_nullable=True)

    # ### end Alembic commands ###
