from typing import Any

from fastapi import APIRouter
from sqlalchemy import select

from src.bookings.schemas import SBookings
from src.database import async_session

from src.bookings.dao import BookingsDAO

router = APIRouter(prefix="/booking", tags=["Бронирование"])


@router.get("", response_model=list[SBookings])
async def retrieve_bookings():
    result = await BookingsDAO.get_all()
    return result


@router.get("/{booking_id}", response_model=SBookings)
async def add_booking_by_id(booking_id: int, model_id: int):
    result = await BookingsDAO.get_by_id(model_id)
    return result


@router.post("/filter", response_model=SBookings)
async def get_booking_by_filter(room_id: int):
    result = await BookingsDAO.get_one_or_none(room_id=room_id)
    return result
