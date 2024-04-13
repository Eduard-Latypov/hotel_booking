from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI, Query

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from src.users.router import router as router_register
from src.hotels.rooms.router import router as hotel_room_router
from src.bookings.router import router as router_booking
from test import router as test_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router_register)
app.include_router(hotel_room_router)
app.include_router(router_booking)
app.include_router(test_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
