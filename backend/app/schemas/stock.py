from pydantic import BaseModel


class StockFilter(BaseModel):
    exchange: str | None = None
    sector: str | None = None
    market_cap_min: float | None = None
    market_cap_max: float | None = None
    pe_max: float | None = None
    roe_min: float | None = None
    debt_to_equity_max: float | None = None


class StockOut(BaseModel):
    symbol: str
    company_name: str
    exchange: str
    sector: str
    market_cap: float
    pe_ratio: float
    roe: float
    debt_to_equity: float
    distance_52w_high: float
    distance_52w_low: float
    volume_spike: float
    last_price: float
    change_pct: float
