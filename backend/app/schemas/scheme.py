from pydantic import BaseModel


class SchemeFilter(BaseModel):
    category: str | None = None
    aum_min: float | None = None
    aum_max: float | None = None
    expense_ratio_max: float | None = None
    return_1y_min: float | None = None
    return_3y_min: float | None = None
    return_5y_min: float | None = None


class SchemeOut(BaseModel):
    code: str
    name: str
    category: str
    aum: float
    expense_ratio: float
    return_1y: float
    return_3y: float
    return_5y: float
    volatility: float
    max_drawdown: float
    nav: float
