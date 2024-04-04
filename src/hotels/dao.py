from sqlalchemy import select

from src.dao import BaseDAO
from .models import Hotels
from src.database import async_session
from .rooms.models import Rooms


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all(cls, location):
        async with async_session() as conn:
            stmt = select(Hotels.__table__.columns).filter(
                Hotels.location.contains(location)
            )
            result = await conn.execute(stmt)
            return result.mappings().all()
