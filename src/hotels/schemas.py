from pydantic import BaseModel, ConfigDict


class SHotelsPOST(BaseModel):
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int


class SHotels(SHotelsPOST):
    id: int

    model_config = ConfigDict(from_attributes=True)
