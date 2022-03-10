"""init

Revision ID: 09c220b82855
Revises: 
Create Date: 2022-02-26 12:02:58.137617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c220b82855'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('describtion', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('describtion', sa.String(), nullable=True),
    sa.Column('oklad', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('client_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_client', sa.Integer(), nullable=False),
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['client.id'], ),
    sa.ForeignKeyConstraint(['id_order'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_employee', sa.Integer(), nullable=False),
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_employee'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['id_order'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_employee', sa.Integer(), nullable=False),
    sa.Column('id_position', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_employee'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['id_position'], ['position.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_position')
    op.drop_table('employee_order')
    op.drop_table('client_order')
    op.drop_table('position')
    op.drop_table('order')
    op.drop_table('employee')
    op.drop_table('client')
    # ### end Alembic commands ###