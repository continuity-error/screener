from abc import ABC, abstractmethod
from datetime import datetime


class MarketProvider(ABC):
    @abstractmethod
    def fetch_indices(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def fetch_stocks(self) -> list[dict]:
        raise NotImplementedError


class SchemeProvider(ABC):
    @abstractmethod
    def fetch_schemes(self) -> list[dict]:
        raise NotImplementedError


class MockMarketProvider(MarketProvider):
    def fetch_indices(self) -> list[dict]:
        now = datetime.utcnow().isoformat()
        return [
            {"index_name": "NIFTY 50", "last_price": 24512.4, "change_pct": 0.78, "captured_at": now},
            {"index_name": "SENSEX", "last_price": 80411.11, "change_pct": 0.69, "captured_at": now},
        ]

    def fetch_stocks(self) -> list[dict]:
        return [
            {
                "symbol": "RELIANCE",
                "company_name": "Reliance Industries",
                "exchange": "NSE",
                "sector": "Energy",
                "market_cap": 19000000,
                "pe_ratio": 22.4,
                "roe": 15.8,
                "debt_to_equity": 0.36,
                "distance_52w_high": -4.2,
                "distance_52w_low": 18.5,
                "volume_spike": 1.2,
                "last_price": 3030.2,
                "change_pct": 1.1,
            }
        ]


class MFToolSchemeProvider(SchemeProvider):
    def fetch_schemes(self) -> list[dict]:
        try:
            from mftool import Mftool

            mf = Mftool()
            data = mf.get_scheme_codes()
            sample = list(data.items())[:50]
            return [
                {
                    "code": str(code),
                    "name": name,
                    "category": "Unknown",
                    "aum": 0,
                    "expense_ratio": 0,
                    "return_1y": 0,
                    "return_3y": 0,
                    "return_5y": 0,
                    "volatility": 0,
                    "max_drawdown": 0,
                    "nav": 0,
                }
                for code, name in sample
            ]
        except Exception:
            return [
                {
                    "code": "MOCK1001",
                    "name": "Mock Large Cap Fund",
                    "category": "Large Cap",
                    "aum": 5000,
                    "expense_ratio": 0.9,
                    "return_1y": 14.1,
                    "return_3y": 13.3,
                    "return_5y": 12.5,
                    "volatility": 9.2,
                    "max_drawdown": -12.2,
                    "nav": 142.3,
                }
            ]
