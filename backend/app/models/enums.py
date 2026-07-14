from enum import StrEnum


class Role(StrEnum):
    ADMIN = "admin"
    ANALYST = "analyst"
    VIEWER = "viewer"


class Exchange(StrEnum):
    NSE = "NSE"
    BSE = "BSE"
