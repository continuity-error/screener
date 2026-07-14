import uuid
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
import structlog
from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging

settings = get_settings()
configure_logging()
logger = structlog.get_logger(__name__)

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title=settings.app_name)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def request_context(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    logger.info("request.complete", request_id=request_id, path=request.url.path, status=response.status_code)
    return response


@app.get("/healthz")
@limiter.limit(settings.rate_limit)
def health(request: Request):
    return {"status": "ok"}


app.include_router(api_router)
