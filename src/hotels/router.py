import asyncio
import datetime


from fastapi import APIRouter
from fastapi_cache.decorator import cache

from .dao import HotelsDAO
from .schemas import SHotels
from .exceptions import AbsentHotel

router = APIRouter(prefix="/hotels", tags=["Отели, Комнаты"])


@router.get("/{location}", response_model=list[SHotels])
@cache(expire=60 * 5)
async def get_hotels(location: str):
    await asyncio.sleep(3)
    result = await HotelsDAO.find_all(location)
    return result


@router.get("/id/{hotel_id}")
async def get_hotel(hotel_id: int):
    hotel = await HotelsDAO.get_one_or_none(id=hotel_id)
    if hotel is None:
        raise AbsentHotel()
    return hotel
