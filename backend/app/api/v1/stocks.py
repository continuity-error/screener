from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.stock import StockFilter, StockOut
from app.services.screeners import query_stocks
import csv
import io

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.get("", response_model=list[StockOut])
def list_stocks(
    exchange: str | None = None,
    sector: str | None = None,
    market_cap_min: float | None = None,
    market_cap_max: float | None = None,
    pe_max: float | None = None,
    roe_min: float | None = None,
    debt_to_equity_max: float | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    db: Session = Depends(get_db),
):
    filters = StockFilter(
        exchange=exchange,
        sector=sector,
        market_cap_min=market_cap_min,
        market_cap_max=market_cap_max,
        pe_max=pe_max,
        roe_min=roe_min,
        debt_to_equity_max=debt_to_equity_max,
    )
    rows = (
        query_stocks(db, filters)
        .order_by("symbol")
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return [StockOut.model_validate(row, from_attributes=True) for row in rows]


@router.get("/export")
def export_stocks(db: Session = Depends(get_db)):
    rows = query_stocks(db, StockFilter()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["symbol", "company_name", "exchange", "sector", "market_cap", "pe_ratio", "roe"])
    for s in rows:
        writer.writerow([s.symbol, s.company_name, s.exchange, s.sector, s.market_cap, s.pe_ratio, s.roe])
    output.seek(0)
    return StreamingResponse(iter([output.getvalue()]), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=stocks.csv"})
