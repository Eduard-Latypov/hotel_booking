import datetime
from typing import Mapping, Any

from passlib.context import CryptContext
import jwt

from src.config import settings
from src.users.dao import UsersDAO

context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return context.hash(password, salt=settings.SECRET_KEY)


def verify_password(password: str, password_hash: str) -> bool:
    return context.verify(password, password_hash)


def create_access_token(data: dict[str, Any]) -> str:
    headers = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    headers.update(exp=expire)
    token = jwt.encode(headers, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token


async def authenticate(email: str, password: str) -> Mapping[str, Any] | None:
    hashed_password = get_password_hash(password)
    user = await UsersDAO.get_one_or_none(email=email, hashed_password=hashed_password)
    return user
