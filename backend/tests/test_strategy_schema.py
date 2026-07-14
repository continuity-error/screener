import pytest
from pydantic import ValidationError
from app.schemas.strategy import StrategyCreate


def test_strategy_name_min_length():
    with pytest.raises(ValidationError):
        StrategyCreate(name="ab", asset_type="stock", rules={})
