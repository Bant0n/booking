from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingRoom, SNewBooking
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
    booking: SNewBooking,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user_id=user.id,
        room_id=booking.room_id,
        date_from=booking.date_from,
        date_to=booking.date_to,
    )

    if not booking:
        raise RoomCannotBeBookedException


@router.delete("/{booking_id}")
async def delete_booking(
    booking_id: int,
    user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(booking_id=booking_id, user_id=user.id)
