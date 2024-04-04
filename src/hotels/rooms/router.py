from src.hotels.router import router
from .dao import RoomsDAO
from .schemas import SRooms


@router.get("/{hotel_id}/rooms", response_model=list[SRooms])
async def get_rooms(hotel_id: int):
    result = await RoomsDAO.get_all(hotel_id=hotel_id)
    return result


@router.post("/{hotel_id}/rooms")
async def add_room(hotel_id: int):
    pass
