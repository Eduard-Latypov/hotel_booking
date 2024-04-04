from src.exceptions import BookingException
from fastapi import status


class InvalidOrEmptyTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Отсутствует или неверный формат токена аутентификации"


class IsAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь с такой почтой уже существует"


class InvalidEmailOrLogin(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"
