"""Add Meal_cards

Revision ID: 83f983b12322
Revises: 
Create Date: 2023-12-13 03:19:49.138490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83f983b12322'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meal_cards',
    sa.Column('meal_id', sa.Integer(), nullable=False),
    sa.Column('meal_served', sa.VARCHAR(length=40), nullable=True),
    sa.Column('specifications', sa.VARCHAR(length=40), nullable=True),
    sa.Column('satisfaction_rank', sa.INTEGER(), nullable=True),
    sa.Column('comments', sa.VARCHAR(length=40), nullable=True),
    sa.Column('barista_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['barista_id'], ['baristas.barista_id'], ),
    sa.PrimaryKeyConstraint('meal_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meal_cards')
    # ### end Alembic commands ###
