from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.cache import get_json, set_json
from app.core.config import get_settings
from app.core.database import get_db
from app.models.market import MarketSnapshot, Stock
from app.schemas.market import MarketSnapshotOut, TickerItem

router = APIRouter(prefix="/market", tags=["market"])
settings = get_settings()


@router.get("/snapshots", response_model=list[MarketSnapshotOut])
def get_snapshots(db: Session = Depends(get_db)):
    cache_key = "market:snapshots"
    cached = get_json(cache_key)
    if cached:
        return cached
    rows = db.query(MarketSnapshot).order_by(MarketSnapshot.index_name).all()
    payload = [MarketSnapshotOut.model_validate(row, from_attributes=True).model_dump() for row in rows]
    set_json(cache_key, payload, settings.market_cache_ttl)
    return payload


@router.get("/ticker", response_model=list[TickerItem])
def get_ticker(db: Session = Depends(get_db)):
    rows = db.query(Stock).order_by(Stock.change_pct.desc()).limit(50).all()
    return [TickerItem.model_validate(row, from_attributes=True) for row in rows]
