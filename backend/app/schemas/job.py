from datetime import datetime
from pydantic import BaseModel


class JobRunOut(BaseModel):
    id: int
    job_name: str
    status: str
    started_at: datetime
    finished_at: datetime | None
    duration_seconds: float | None
    summary: str | None
