from pydantic import BaseModel, Field


class StrategyCreate(BaseModel):
    name: str = Field(min_length=3, max_length=120)
    asset_type: str
    rules: dict


class StrategyOut(BaseModel):
    id: int
    name: str
    asset_type: str
    rules: dict


class StrategyExecutionOut(BaseModel):
    strategy_id: int
    matches: list[dict]
