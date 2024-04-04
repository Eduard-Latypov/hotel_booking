from src.exceptions import BookingException
from fastapi import status


class AbsentHotel(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Отель с таким ID отсутствует"
