"""updated admin table and added jobs_list table

Revision ID: 4231608f93b8
Revises: 4e4893b4a39a
Create Date: 2025-01-05 19:29:24.337373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4231608f93b8'
down_revision: Union[str, None] = '4e4893b4a39a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_login_id'), 'admin_login', ['id'], unique=False)
    op.create_index(op.f('ix_admin_login_uname'), 'admin_login', ['uname'], unique=False)
    op.create_table('jobs_list',
    sa.Column('job_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('job_role', sa.String(), nullable=False),
    sa.Column('job_description', sa.String(), nullable=True),
    sa.Column('career_page_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('job_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs_list')
    op.drop_index(op.f('ix_admin_login_uname'), table_name='admin_login')
    op.drop_index(op.f('ix_admin_login_id'), table_name='admin_login')
    op.drop_table('admin_login')
    # ### end Alembic commands ###
