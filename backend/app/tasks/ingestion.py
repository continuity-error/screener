from celery.utils.log import get_task_logger
from tenacity import retry, stop_after_attempt, wait_exponential
from app.core.celery_app import celery_app
from app.core.database import SessionLocal
from app.services.ingestion import ingest_market_data, ingest_scheme_data
from app.services.provider import MFToolSchemeProvider, MockMarketProvider

logger = get_task_logger(__name__)


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=30))
def refresh_market_data(self):
    db = SessionLocal()
    try:
        ingest_market_data(db, MockMarketProvider())
        return {"status": "ok"}
    finally:
        db.close()


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=30))
def refresh_scheme_data(self):
    db = SessionLocal()
    try:
        ingest_scheme_data(db, MFToolSchemeProvider())
        return {"status": "ok"}
    finally:
        db.close()
