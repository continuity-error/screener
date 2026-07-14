from pydantic import ValidationError
from app.schemas.strategy import StrategyCreate


def test_strategy_name_min_length():
    try:
        StrategyCreate(name="ab", asset_type="stock", rules={})
        assert False
    except ValidationError:
        assert True
