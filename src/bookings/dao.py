from sqlalchemy import select, and_, or_, func, insert

from src.dao import BaseDAO
from .models import Bookings
from src.hotels.rooms.dao import RoomsDAO
from src.database import async_session


class BookingsDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(
        cls,
        user_id,
        room_id,
        date_from,
        date_to,
    ):
        booking_stmt = select(func.count(Bookings.room_id)).filter(
            and_(
                Bookings.room_id == room_id,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to,
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to >= date_from,
                    ),
                ),
            )
        )
        rooms = await RoomsDAO.get_by_id(model_id=room_id)
        if rooms is None:
            return
        room_quantity, room_price = rooms.get("quantity"), rooms.get("price")

        async with async_session() as conn:
            result = await conn.execute(booking_stmt)
            bookings = result.scalar()
            if (room_quantity - bookings) > 0:
                res = await super().add(
                    user_id=user_id,
                    room_id=room_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=room_price,
                )
                return res
