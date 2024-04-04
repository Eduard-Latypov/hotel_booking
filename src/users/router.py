from fastapi import APIRouter, Response, Depends

from src.users.auth import get_password_hash, authenticate, create_access_token

from src.users.dao import UsersDAO
from src.users.schemas import SUserAuth, SUsers
from .dependencies import get_current_user
from .exceptions import IsAlreadyExistsException, InvalidEmailOrLogin

router = APIRouter(prefix="/auth", tags=["Auth & Пользователи"])


@router.post("/register")
async def register(user_data: SUserAuth):
    user = await UsersDAO.get_one_or_none(email=user_data.email)
    if user:
        raise IsAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    response = await UsersDAO.add(
        email=user_data.email, hashed_password=hashed_password
    )
    return response


@router.post("/login")
async def user_login(response: Response, user_data: SUserAuth):
    user = await authenticate(user_data.email, user_data.password)
    if not user:
        raise InvalidEmailOrLogin()
    access_token = create_access_token({"sub": str(user["id"])})
    response.set_cookie("access_token", access_token, httponly=True)
    return {
        "message": "Congratulation, you are is authenticated",
        "access_token": access_token,
    }


@router.get("/users", response_model=SUsers)
async def get_user(user_id: int = Depends(get_current_user)):
    user = await UsersDAO.get_one_or_none(id=user_id)
    return user
