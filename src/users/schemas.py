from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi import Body


class SUsers(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)


class SUserAuth(BaseModel):
    email: EmailStr
    password: Annotated[str, Body(min_length=8)]
