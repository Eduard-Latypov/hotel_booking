import datetime
from typing import Mapping, Any

from fastapi import Depends, Request, HTTPException, status, Cookie
import jwt

from config import settings
from .dao import UsersDAO
from .exceptions import InvalidOrEmptyTokenException


def get_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if token is None:
        raise InvalidOrEmptyTokenException()
    return token


def get_current_user(token: str = Depends(get_token)) -> int:
    try:
        payload = jwt.decode(
            token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        raise InvalidOrEmptyTokenException
    return int(payload["sub"])
