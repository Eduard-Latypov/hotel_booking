from src.dao import BaseDAO
from .models import Bookings


class BookingsDAO(BaseDAO):
    model = Bookings
