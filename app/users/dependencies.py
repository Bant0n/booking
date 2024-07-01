from datetime import datetime
from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError

from app.config import settings
from app.users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Необходима авторизация",
        )
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, key=settings.KEY, algorithms=settings.ALGORITHM
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    user = await UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return user