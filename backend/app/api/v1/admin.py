from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.api.deps import require_admin
from app.core.database import get_db
from app.models.audit import AuditLog
from app.models.market import Stock
from app.models.scheme import Scheme
from app.tasks.ingestion import refresh_market_data, refresh_scheme_data

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/run-import")
def run_import_now(db: Session = Depends(get_db), admin=Depends(require_admin)):
    market_job = refresh_market_data.delay()
    scheme_job = refresh_scheme_data.delay()
    db.add(AuditLog(actor=admin.email, action="run_import", details="Triggered market and scheme refresh"))
    db.commit()
    return {"market_task_id": market_job.id, "scheme_task_id": scheme_job.id}


@router.get("/data-quality")
def data_quality(db: Session = Depends(get_db), _=Depends(require_admin)):
    stale_schemes = db.query(Scheme).filter(Scheme.nav == 0).count()
    missing_sector = db.query(Stock).filter((Stock.sector == "") | (Stock.sector.is_(None))).count()
    duplicates = (
        db.query(Stock.symbol)
        .group_by(Stock.symbol)
        .having(func.count(Stock.symbol) > 1)
        .count()
    )
    return {
        "stale_scheme_rows": stale_schemes,
        "stocks_missing_sector": missing_sector,
        "duplicate_stock_symbols": duplicates,
    }
