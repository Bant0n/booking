from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingRoom
from app.exceptions import RoomCannotBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Бронирования"])


@router.get("")
async def get_bookings(
    user: Users = Depends(get_current_user),
) -> list[SBookingRoom]:
    return await BookingDAO.find_by_user(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to
    )

    if not booking:
        raise RoomCannotBeBookedException
