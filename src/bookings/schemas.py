import datetime

from pydantic import BaseModel, ConfigDict


class SBookings(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: datetime.date
    date_to: datetime.date
    price: int
    total_cost: int | None
    total_days: int | None

    model_config = ConfigDict(from_attributes=True)
