from dataclasses import dataclass
import datetime
from typing import Annotated, Optional, Any

from fastapi import Query, Body
from pydantic import (
    BaseModel,
    field_validator,
    ValidationError,
    validator,
    model_validator,
)


@dataclass
class HotelData:
    location: str
    date_from: datetime.date
    date_to: datetime.date
    has_spa: Annotated[bool, Query()] = None
    rating: Annotated[int, Query(ge=1, le=5)] = None


class SBooking(BaseModel):
    room_id: int
    date_from: datetime.date
    date_to: datetime.date

    @field_validator("date_to")
    @classmethod
    def validate_date_to(cls, value, values):
        if value >= values.data["date_from"]:
            return value
        raise ValueError("Дата выезда должна быть позднее даты въезда")
