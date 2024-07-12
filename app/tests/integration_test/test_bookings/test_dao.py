from datetime import datetime
from app.bookings.dao import BookingDAO


async def test_add_and_get_booking():
    new_booking = await BookingDAO.add(
        user_id=1,
        room_id=1,
        date_from=datetime.strptime("2024-7-12", "%Y-%m-%d"),
        date_to=datetime.strptime("2024-8-20", "%Y-%m-%d"),
    )
    assert new_booking.user_id == 1
    assert new_booking.room_id == 1

    new_booking = await BookingDAO.find_one_or_none(id=new_booking.id)

    assert new_booking is not None
