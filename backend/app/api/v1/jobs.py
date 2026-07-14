from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job import JobRun
from app.schemas.job import JobRunOut

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/history", response_model=list[JobRunOut])
def get_job_history(db: Session = Depends(get_db)):
    rows = db.query(JobRun).order_by(JobRun.started_at.desc()).limit(100).all()
    return [JobRunOut.model_validate(row, from_attributes=True) for row in rows]
