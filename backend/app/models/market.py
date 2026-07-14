from datetime import datetime, timezone
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class MarketSnapshot(Base):
    __tablename__ = "market_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True)
    index_name: Mapped[str] = mapped_column(String(64), index=True)
    last_price: Mapped[float] = mapped_column(Float)
    change_pct: Mapped[float] = mapped_column(Float)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True
    )


class Stock(Base):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str] = mapped_column(String(32), index=True)
    company_name: Mapped[str] = mapped_column(String(255))
    exchange: Mapped[str] = mapped_column(String(8), index=True)
    sector: Mapped[str] = mapped_column(String(64), index=True)
    market_cap: Mapped[float] = mapped_column(Float, default=0)
    pe_ratio: Mapped[float] = mapped_column(Float, default=0)
    roe: Mapped[float] = mapped_column(Float, default=0)
    debt_to_equity: Mapped[float] = mapped_column(Float, default=0)
    distance_52w_high: Mapped[float] = mapped_column(Float, default=0)
    distance_52w_low: Mapped[float] = mapped_column(Float, default=0)
    volume_spike: Mapped[float] = mapped_column(Float, default=0)
    last_price: Mapped[float] = mapped_column(Float, default=0)
    change_pct: Mapped[float] = mapped_column(Float, default=0)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
