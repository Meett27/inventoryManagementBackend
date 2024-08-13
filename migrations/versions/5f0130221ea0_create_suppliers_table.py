"""Create suppliers table

Revision ID: 5f0130221ea0
Revises: c5246ab0feb0
Create Date: 2024-08-13 18:51:59.646436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f0130221ea0'
down_revision = 'c5246ab0feb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suppliers',
    sa.Column('SupplierID', sa.Integer(), nullable=False),
    sa.Column('CompanyName', sa.String(length=100), nullable=False),
    sa.Column('ContactFname', sa.String(length=50), nullable=False),
    sa.Column('ContactLname', sa.String(length=50), nullable=False),
    sa.Column('ContactTitle', sa.String(length=50), nullable=True),
    sa.Column('Address', sa.String(length=200), nullable=True),
    sa.Column('Phone', sa.String(length=20), nullable=True),
    sa.Column('Fax', sa.String(length=20), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('PaymentMethods', sa.String(length=100), nullable=True),
    sa.Column('DiscountType', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('SupplierID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suppliers')
    # ### end Alembic commands ###
