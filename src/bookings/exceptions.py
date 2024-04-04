from src.exceptions import BookingException
from fastapi import status


class EmptyForBooking(BookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Такая комната отсутствует либо недоступна для бронирования"


class ForbiddenOrAbsentBooking(BookingException):
    status = status.HTTP_403_FORBIDDEN
    detail = "Такая бронь отсутствует либо у пользователя недостаточно прав для удаления этой брони"
