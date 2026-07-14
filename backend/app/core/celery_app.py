from celery import Celery
from app.core.config import get_settings

settings = get_settings()
celery_app = Celery("screener", broker=settings.redis_url, backend=settings.redis_url)
celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    timezone="Asia/Kolkata",
    beat_schedule={
        "refresh-market-data": {
            "task": "app.tasks.ingestion.refresh_market_data",
            "schedule": 300.0,
        },
        "refresh-scheme-data": {
            "task": "app.tasks.ingestion.refresh_scheme_data",
            "schedule": 3600.0,
        },
    },
)
celery_app.autodiscover_tasks(["app.tasks"])
