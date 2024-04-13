from typing import Type, Sequence, Mapping, Any

from sqlalchemy import select, insert, delete, text
from .database import Base
from src.database import async_session


class BaseDAO:
    model: Type[Base]

    @classmethod
    async def get_all(cls, **filter_by) -> list[Mapping[str, Any]]:
        async with async_session() as conn:
            stmt = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await conn.execute(stmt)
            return result.mappings().all()

    @classmethod
    async def get_one_or_none(cls, **filter_by: Any) -> Mapping[str, Any] | None:
        async with async_session() as conn:
            stmt = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await conn.execute(stmt)
            return result.mappings().one_or_none()

    @classmethod
    async def get_by_id(cls, model_id: int) -> Mapping[str, Any] | None:
        async with async_session() as conn:
            stmt = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await conn.execute(stmt)
            return result.mappings().one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session() as conn:
            stmt = insert(cls.model).values(**data)
            result = await conn.execute(stmt.returning(cls.model.__table__.columns))
            await conn.commit()
            return result.mappings().one_or_none()

    @classmethod
    async def delete_record(cls, **filter_by):
        async with async_session() as conn:
            stmt = delete(cls.model).filter_by(**filter_by).returning(cls.model.id)
            result = await conn.execute(stmt)
            ids = result.mappings().one()
            await conn.commit()
            return ids
