from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, Header, Request

from typing import Annotated


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login")


router = APIRouter(prefix="/test_auth", tags=["auth"])


@router.post("")
async def auth(token: Annotated[str, Depends(oauth2_schema)]):
    return {"token": token}
