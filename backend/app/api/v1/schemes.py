from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.scheme import SchemeFilter, SchemeOut
from app.services.screeners import query_schemes

router = APIRouter(prefix="/schemes", tags=["schemes"])


@router.get("", response_model=list[SchemeOut])
def list_schemes(
    category: str | None = None,
    aum_min: float | None = None,
    aum_max: float | None = None,
    expense_ratio_max: float | None = None,
    return_1y_min: float | None = None,
    return_3y_min: float | None = None,
    return_5y_min: float | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    db: Session = Depends(get_db),
):
    filters = SchemeFilter(
        category=category,
        aum_min=aum_min,
        aum_max=aum_max,
        expense_ratio_max=expense_ratio_max,
        return_1y_min=return_1y_min,
        return_3y_min=return_3y_min,
        return_5y_min=return_5y_min,
    )
    rows = (
        query_schemes(db, filters)
        .order_by("name")
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return [SchemeOut.model_validate(row, from_attributes=True) for row in rows]
