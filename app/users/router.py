from fastapi import APIRouter, HTTPException

from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.schemas import SUserAuth


router = APIRouter(
    prefix="/users",
    tags=["Auth & Пользователи"],
)


@router.post("/register")
async def register_uer(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise HTTPException(
            status_code=401, detail="Пользователь уже существует"
        )

    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.get('/users')
async def get_users():
    return await UserDAO.find_all()
