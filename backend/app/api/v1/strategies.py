from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.market import Stock
from app.models.scheme import Scheme
from app.models.strategy import Strategy
from app.models.user import User
from app.schemas.strategy import StrategyCreate, StrategyExecutionOut, StrategyOut

router = APIRouter(prefix="/strategies", tags=["strategies"])


@router.post("", response_model=StrategyOut)
def create_strategy(payload: StrategyCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    strategy = Strategy(name=payload.name, asset_type=payload.asset_type, rules=payload.rules, created_by_id=user.id)
    db.add(strategy)
    db.commit()
    db.refresh(strategy)
    return StrategyOut.model_validate(strategy, from_attributes=True)


@router.get("", response_model=list[StrategyOut])
def list_strategies(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    rows = db.query(Strategy).order_by(Strategy.id.desc()).all()
    return [StrategyOut.model_validate(row, from_attributes=True) for row in rows]


@router.post("/{strategy_id}/execute", response_model=StrategyExecutionOut)
def execute_strategy(strategy_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")

    rules = strategy.rules or {}
    matches = []
    if strategy.asset_type == "stock":
        q = db.query(Stock)
        if rules.get("roe_gt") is not None:
            q = q.filter(Stock.roe > float(rules["roe_gt"]))
        if rules.get("return_3y_gt") is not None:
            q = q.filter(Stock.change_pct > float(rules["return_3y_gt"]))
        for s in q.limit(100).all():
            matches.append({"name": s.symbol, "score": s.roe + s.change_pct})
    elif strategy.asset_type == "scheme":
        q = db.query(Scheme)
        if rules.get("return_3y_gt") is not None:
            q = q.filter(Scheme.return_3y > float(rules["return_3y_gt"]))
        if rules.get("expense_ratio_lt") is not None:
            q = q.filter(Scheme.expense_ratio < float(rules["expense_ratio_lt"]))
        for f in q.limit(100).all():
            matches.append({"name": f.name, "score": f.return_3y - f.expense_ratio})
    matches.sort(key=lambda x: x["score"], reverse=True)
    return StrategyExecutionOut(strategy_id=strategy_id, matches=matches)
