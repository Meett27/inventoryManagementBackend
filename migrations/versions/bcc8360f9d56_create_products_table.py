"""Create products table

Revision ID: bcc8360f9d56
Revises: 5f0130221ea0
Create Date: 2024-08-14 20:14:15.628001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcc8360f9d56'
down_revision = '5f0130221ea0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('ProductID', sa.Integer(), nullable=False),
    sa.Column('ProductName', sa.String(length=100), nullable=False),
    sa.Column('ProductDescription', sa.String(length=255), nullable=True),
    sa.Column('SupplierID', sa.Integer(), nullable=False),
    sa.Column('CategoryID', sa.Integer(), nullable=False),
    sa.Column('QuantityPerUnit', sa.String(length=50), nullable=True),
    sa.Column('UnitPrice', sa.Float(), nullable=True),
    sa.Column('UnitWeight', sa.Float(), nullable=True),
    sa.Column('Size', sa.String(length=50), nullable=True),
    sa.Column('Discount', sa.Float(), nullable=True),
    sa.Column('UnitsInStock', sa.Integer(), nullable=True),
    sa.Column('UnitsonOrder', sa.Integer(), nullable=True),
    sa.Column('ReorderLevel', sa.Integer(), nullable=True),
    sa.Column('ProductAvailable', sa.Boolean(), nullable=True),
    sa.Column('Note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['SupplierID'], ['suppliers.SupplierID'], ),
    sa.PrimaryKeyConstraint('ProductID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
