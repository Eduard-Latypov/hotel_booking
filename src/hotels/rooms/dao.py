from src.dao import BaseDAO
from .models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms
