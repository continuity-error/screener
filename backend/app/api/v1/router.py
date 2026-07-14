from fastapi import APIRouter
from app.api.v1 import admin, auth, jobs, market, schemes, stocks, strategies

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(market.router)
api_router.include_router(stocks.router)
api_router.include_router(schemes.router)
api_router.include_router(strategies.router)
api_router.include_router(jobs.router)
api_router.include_router(admin.router)
