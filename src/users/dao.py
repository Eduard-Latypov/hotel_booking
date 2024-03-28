from src.dao import BaseDAO
from .models import Users


class UsersDAO(BaseDAO):
    model = Users
