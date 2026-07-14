"""initial schema"""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("role", sa.Enum("ADMIN", "ANALYST", "VIEWER", name="role"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "market_snapshots",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("index_name", sa.String(length=64), nullable=False),
        sa.Column("last_price", sa.Float(), nullable=False),
        sa.Column("change_pct", sa.Float(), nullable=False),
        sa.Column("captured_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_market_snapshots_index_name", "market_snapshots", ["index_name"], unique=False)

    op.create_table(
        "stocks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("symbol", sa.String(length=32), nullable=False),
        sa.Column("company_name", sa.String(length=255), nullable=False),
        sa.Column("exchange", sa.String(length=8), nullable=False),
        sa.Column("sector", sa.String(length=64), nullable=False),
        sa.Column("market_cap", sa.Float(), nullable=False),
        sa.Column("pe_ratio", sa.Float(), nullable=False),
        sa.Column("roe", sa.Float(), nullable=False),
        sa.Column("debt_to_equity", sa.Float(), nullable=False),
        sa.Column("distance_52w_high", sa.Float(), nullable=False),
        sa.Column("distance_52w_low", sa.Float(), nullable=False),
        sa.Column("volume_spike", sa.Float(), nullable=False),
        sa.Column("return_3y", sa.Float(), nullable=False),
        sa.Column("last_price", sa.Float(), nullable=False),
        sa.Column("change_pct", sa.Float(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_stocks_symbol", "stocks", ["symbol"], unique=False)
    op.create_index("ix_stocks_exchange", "stocks", ["exchange"], unique=False)
    op.create_index("ix_stocks_sector", "stocks", ["sector"], unique=False)

    op.create_table(
        "schemes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("category", sa.String(length=64), nullable=False),
        sa.Column("aum", sa.Float(), nullable=False),
        sa.Column("expense_ratio", sa.Float(), nullable=False),
        sa.Column("return_1y", sa.Float(), nullable=False),
        sa.Column("return_3y", sa.Float(), nullable=False),
        sa.Column("return_5y", sa.Float(), nullable=False),
        sa.Column("volatility", sa.Float(), nullable=False),
        sa.Column("max_drawdown", sa.Float(), nullable=False),
        sa.Column("nav", sa.Float(), nullable=False),
        sa.Column("nav_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_schemes_code", "schemes", ["code"], unique=True)
    op.create_index("ix_schemes_name", "schemes", ["name"], unique=False)
    op.create_index("ix_schemes_category", "schemes", ["category"], unique=False)

    op.create_table(
        "strategies",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("asset_type", sa.String(length=16), nullable=False),
        sa.Column("rules", sa.JSON(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_strategies_name", "strategies", ["name"], unique=True)

    op.create_table(
        "job_runs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("job_name", sa.String(length=120), nullable=False),
        sa.Column("status", sa.String(length=24), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("duration_seconds", sa.Float(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
    )
    op.create_index("ix_job_runs_job_name", "job_runs", ["job_name"], unique=False)
    op.create_index("ix_job_runs_status", "job_runs", ["status"], unique=False)

    op.create_table(
        "audit_logs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("actor", sa.String(length=255), nullable=False),
        sa.Column("action", sa.String(length=255), nullable=False),
        sa.Column("details", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_audit_logs_actor", "audit_logs", ["actor"], unique=False)
    op.create_index("ix_audit_logs_action", "audit_logs", ["action"], unique=False)


def downgrade() -> None:
    op.drop_table("audit_logs")
    op.drop_table("job_runs")
    op.drop_table("strategies")
    op.drop_table("schemes")
    op.drop_table("stocks")
    op.drop_table("market_snapshots")
    op.drop_table("users")
    op.execute("DROP TYPE IF EXISTS role")
