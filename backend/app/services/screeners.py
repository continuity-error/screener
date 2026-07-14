from sqlalchemy.orm import Session
from app.models.market import Stock
from app.models.scheme import Scheme
from app.schemas.scheme import SchemeFilter
from app.schemas.stock import StockFilter


def query_stocks(db: Session, filters: StockFilter):
    q = db.query(Stock)
    if filters.exchange:
        q = q.filter(Stock.exchange == filters.exchange)
    if filters.sector:
        q = q.filter(Stock.sector == filters.sector)
    if filters.market_cap_min is not None:
        q = q.filter(Stock.market_cap >= filters.market_cap_min)
    if filters.market_cap_max is not None:
        q = q.filter(Stock.market_cap <= filters.market_cap_max)
    if filters.pe_max is not None:
        q = q.filter(Stock.pe_ratio <= filters.pe_max)
    if filters.roe_min is not None:
        q = q.filter(Stock.roe >= filters.roe_min)
    if filters.debt_to_equity_max is not None:
        q = q.filter(Stock.debt_to_equity <= filters.debt_to_equity_max)
    return q


def query_schemes(db: Session, filters: SchemeFilter):
    q = db.query(Scheme)
    if filters.category:
        q = q.filter(Scheme.category == filters.category)
    if filters.aum_min is not None:
        q = q.filter(Scheme.aum >= filters.aum_min)
    if filters.aum_max is not None:
        q = q.filter(Scheme.aum <= filters.aum_max)
    if filters.expense_ratio_max is not None:
        q = q.filter(Scheme.expense_ratio <= filters.expense_ratio_max)
    if filters.return_1y_min is not None:
        q = q.filter(Scheme.return_1y >= filters.return_1y_min)
    if filters.return_3y_min is not None:
        q = q.filter(Scheme.return_3y >= filters.return_3y_min)
    if filters.return_5y_min is not None:
        q = q.filter(Scheme.return_5y >= filters.return_5y_min)
    return q
