from src.dao import BaseDAO
from .models import Hotels


class HotelsDAO(BaseDAO):
    model = Hotels
