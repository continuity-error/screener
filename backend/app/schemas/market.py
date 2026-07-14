from datetime import datetime
from pydantic import BaseModel


class MarketSnapshotOut(BaseModel):
    index_name: str
    last_price: float
    change_pct: float
    captured_at: datetime


class TickerItem(BaseModel):
    symbol: str
    last_price: float
    change_pct: float
