"""empty message

Revision ID: 3896284d19c6
Revises: 1111d67fa788
Create Date: 2021-01-07 12:28:42.225583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3896284d19c6'
down_revision = '1111d67fa788'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('localstore',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('store_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('address_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_localstore_id'), 'localstore', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_localstore_id'), table_name='localstore')
    op.drop_table('localstore')
    # ### end Alembic commands ###