from datetime import datetime, timezone
import pandas as pd
from sqlalchemy.orm import Session
from app.models.job import JobRun
from app.models.market import MarketSnapshot, Stock
from app.models.scheme import Scheme
from app.services.provider import MarketProvider, SchemeProvider


def _start_job(db: Session, name: str) -> JobRun:
    run = JobRun(job_name=name, status="running")
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


def _finish_job(db: Session, run: JobRun, summary: str, status: str = "success") -> None:
    now = datetime.now(timezone.utc)
    run.status = status
    run.finished_at = now
    run.duration_seconds = (now - run.started_at).total_seconds()
    run.summary = summary
    db.add(run)
    db.commit()


def ingest_market_data(db: Session, provider: MarketProvider) -> None:
    run = _start_job(db, "market_refresh")
    try:
        indices_df = pd.DataFrame(provider.fetch_indices())
        stocks_df = pd.DataFrame(provider.fetch_stocks())

        db.query(MarketSnapshot).delete()
        db.query(Stock).delete()

        for row in indices_df.to_dict(orient="records"):
            db.add(MarketSnapshot(**row))

        for row in stocks_df.to_dict(orient="records"):
            db.add(Stock(**row))

        db.commit()
        _finish_job(db, run, f"Imported {len(indices_df)} indices and {len(stocks_df)} stocks")
    except Exception as exc:
        db.rollback()
        _finish_job(db, run, f"Import failed: {exc}", "failed")
        raise


def ingest_scheme_data(db: Session, provider: SchemeProvider) -> None:
    run = _start_job(db, "scheme_refresh")
    try:
        schemes_df = pd.DataFrame(provider.fetch_schemes())
        if not schemes_df.empty:
            schemes_df = schemes_df.fillna(0)
        for row in schemes_df.to_dict(orient="records"):
            scheme = db.query(Scheme).filter(Scheme.code == row["code"]).first()
            if scheme:
                for key, value in row.items():
                    setattr(scheme, key, value)
            else:
                db.add(Scheme(**row))
        db.commit()
        _finish_job(db, run, f"Upserted {len(schemes_df)} schemes")
    except Exception as exc:
        db.rollback()
        _finish_job(db, run, f"Import failed: {exc}", "failed")
        raise
