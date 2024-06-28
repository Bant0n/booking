from fastapi import APIRouter, HTTPException, Response

from app.users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from app.users.dao import UserDAO
from app.users.schemas import SUserAuth


router = APIRouter(
    prefix="/users",
    tags=["Auth & Пользователи"],
)


@router.get("/users")
async def get_users():
    return await UserDAO.find_all()


@router.post("/register")
async def register_uer(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise HTTPException(
            status_code=401, detail="Пользователь уже существует"
        )

    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)

    if not user:
        raise HTTPException(
            status_code=401, detail="Неправильные данные для входа"
        )

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token
