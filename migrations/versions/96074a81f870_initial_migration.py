"""initial migration

Revision ID: 96074a81f870
Revises: 
Create Date: 2017-07-06 19:34:52.461893

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '96074a81f870'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('ein', sa.String(length=4), nullable=False),
    sa.Column('parent_ein', sa.String(length=3), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('acronym', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('ein')
    )
    op.create_table('auth_user',
    sa.Column('guid', sa.String(length=64), nullable=False),
    sa.Column('auth_type', sa.Enum('EDIRSSO', 'Saml2In:NYC Employees', 'FacebookSSO', 'MSLiveSSO', 'YahooSSO', 'LinkedInSSO', 'GoogleSSO', name='user_auth_type'), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('middle_initial', sa.String(length=1), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.Column('email_validated', sa.Boolean(), nullable=False),
    sa.Column('terms_of_use_accepted', sa.Boolean(), nullable=False),
    sa.Column('is_poc', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_super', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('guid', 'auth_type'),
    sa.UniqueConstraint('email')
    )
    op.create_table('report_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('value', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('value')
    )
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_guid', sa.String(length=64), nullable=False),
    sa.Column('user_auth_type', sa.Enum('EDIRSSO', 'Saml2In:NYC Employees', 'FacebookSSO', 'MSLiveSSO', 'YahooSSO', 'LinkedInSSO', 'GoogleSSO', name='user_auth_type'), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('subtitle', sa.String(length=150), nullable=True),
    sa.Column('names', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('report_type', sa.String(length=64), nullable=False),
    sa.Column('language', sa.Enum('english', 'spanish', 'chinese', 'russian', 'arabic', 'bengali', 'french', 'haitian_creole', 'italian', 'korean', 'polish', 'urdu', 'yiddish', name='language'), nullable=False),
    sa.Column('subjects', postgresql.ARRAY(sa.String(length=120)), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('date_published', sa.DateTime(), nullable=True),
    sa.Column('report_year_type', sa.Enum('calendar', 'fiscal', 'other', name='year_type'), nullable=False),
    sa.Column('report_year_start', sa.DateTime(), nullable=False),
    sa.Column('report_year_end', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('published', 'submitted', 'resubmitted', 'saved', 'changes_requested', 'approved', name='document_action'), nullable=False),
    sa.ForeignKeyConstraint(['report_type'], ['report_type.value'], ),
    sa.ForeignKeyConstraint(['user_guid', 'user_auth_type'], ['auth_user.guid', 'auth_user.auth_type'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id', 'report_type')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_guid', sa.String(length=64), nullable=False),
    sa.Column('user_auth_type', sa.Enum('EDIRSSO', 'Saml2In:NYC Employees', 'FacebookSSO', 'MSLiveSSO', 'YahooSSO', 'LinkedInSSO', 'GoogleSSO', name='user_auth_type'), nullable=False),
    sa.Column('type', sa.Enum('document', 'registration', name='event_type'), nullable=False),
    sa.ForeignKeyConstraint(['user_guid', 'user_auth_type'], ['auth_user.guid', 'auth_user.auth_type'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_guid', sa.String(length=64), nullable=False),
    sa.Column('user_auth_type', sa.Enum('EDIRSSO', 'Saml2In:NYC Employees', 'FacebookSSO', 'MSLiveSSO', 'YahooSSO', 'LinkedInSSO', 'GoogleSSO', name='user_auth_type'), nullable=False),
    sa.Column('agency_ein', sa.String(length=4), nullable=False),
    sa.ForeignKeyConstraint(['agency_ein'], ['agency.ein'], ),
    sa.ForeignKeyConstraint(['user_guid', 'user_auth_type'], ['auth_user.guid', 'auth_user.auth_type'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.Enum('published', 'submitted', 'resubmitted', 'saved', 'changes_requested', 'approved', name='document_action'), nullable=False),
    sa.Column('state', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['document_id'], ['document.id'], ),
    sa.ForeignKeyConstraint(['id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registration_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.Enum('submitted', 'denied', 'approved', name='registration_action'), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['registration_id'], ['registration.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('registration_id', 'action')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hash', sa.String(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['document_id'], ['document.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    op.drop_table('event_registration')
    op.drop_table('event_document')
    op.drop_table('registration')
    op.drop_table('event')
    op.drop_table('document')
    op.drop_table('report_type')
    op.drop_table('auth_user')
    op.drop_table('agency')
    # ### end Alembic commands ###
