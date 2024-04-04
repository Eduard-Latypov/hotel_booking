import datetime

from sqlalchemy import ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import UniqueConstraint

from src.database import Base


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    # hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    date_to: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    # __table_args__ = UniqueConstraint(
    #     "room_id", "hotel_id", "date_from", "date_to", name="room_date_unq"
    # )

    def __str__(self):
        return f"Booking #{self.id}"
