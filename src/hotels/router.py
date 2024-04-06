import asyncio
from typing import Annotated

import aiofiles
import datetime


from fastapi import APIRouter, UploadFile, Depends, File
from fastapi_cache.decorator import cache

from .dao import HotelsDAO
from .schemas import SHotels, SHotelsPOST
from .exceptions import AbsentHotel

router = APIRouter(prefix="/hotels", tags=["Отели, Комнаты"])


@router.get("/{location}", response_model=list[SHotels])
@cache(expire=60 * 5)
async def get_hotels(location: str):
    await asyncio.sleep(3)
    result = await HotelsDAO.find_all(location)
    return result


@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int):
    hotel = await HotelsDAO.get_one_or_none(id=hotel_id)
    if hotel is None:
        raise AbsentHotel()
    return hotel


@router.post("")
async def add_hotel(hotel_data: SHotelsPOST):
    hotel = await HotelsDAO.add(
        name=hotel_data.name,
        location=hotel_data.location,
        services=hotel_data.services,
        rooms_quantity=hotel_data.rooms_quantity,
        image_id=hotel_data.image_id,
    )
    hotel_id = hotel.get("id")
    return hotel_id


@router.post("/file")
async def add_hotel_image(hotel_id: int, image: UploadFile):
    async with aiofiles.open(f"src/hotels/images/{hotel_id}.webp", "wb+") as file:
        image_file = await image.read()
        await file.write(image_file)
    return {"message": "everything is ok"}
