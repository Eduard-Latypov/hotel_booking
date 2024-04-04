import datetime
from typing import Any

from fastapi import APIRouter, Request, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.bookings.schemas import SBookings
from src.database import async_session

from src.users.dependencies import get_current_user


from .dao import BookingsDAO
from .models import Bookings
from .exceptions import EmptyForBooking, ForbiddenOrAbsentBooking

router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("", response_model=list[SBookings])
async def get_my_bookings(user_id: int = Depends(get_current_user)):
    bookings = await BookingsDAO.get_all(user_id=user_id)
    return bookings


@router.post("")
async def add_booking(
    room_id: int,
    date_from: datetime.date,
    date_to: datetime.date,
    user_id: int = Depends(get_current_user),
):
    result = await BookingsDAO.add(user_id, room_id, date_from, date_to)
    if result is None:
        raise EmptyForBooking()
    return result


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, user_id: int = Depends(get_current_user)):
    try:
        res = await BookingsDAO.delete_record(user_id=user_id, id=booking_id)
        message = f"Бронирование с {res} успешно удалено"
        return {"message": message}
    except NoResultFound:
        raise ForbiddenOrAbsentBooking()
