from fastapi import APIRouter, HTTPException, status, Response

from src.users.auth import get_password_hash, authenticate, create_access_token

from src.users.dao import UsersDAO
from src.users.schemas import SUserRegister, SUsers

router = APIRouter(prefix="/auth", tags=["Auth & Пользователи"])


@router.post("/register")
async def register(user_data: SUserRegister):
    user = await UsersDAO.get_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    hashed_password = get_password_hash(user_data.password)
    response = await UsersDAO.add(
        email=user_data.email, hashed_password=hashed_password
    )
    return response.mappings().one()


@router.post("/login")
async def user_login(response: Response, user_data: SUserRegister):
    user = await authenticate(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный пароль или логин"
        )
    access_token = create_access_token({"sub": user["id"]})
    response.set_cookie("access_token", access_token, httponly=True)
    return {
        "message": "Congratulation, you are is authenticated",
        "access_token": access_token,
    }


@router.get("/users/{user_id}", response_model=SUsers)
async def get_user(user_id: int):
    user = await UsersDAO.get_one_or_none(id=user_id)
    return user
