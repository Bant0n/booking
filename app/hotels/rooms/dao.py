from datetime import date
from sqlalchemy import and_, func, or_, select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(
        cls,
        hotel_id: int,
        date_from: date,
        date_to: date,
    ):
        """
        with booked_rooms as (
            select room_id, count(room_id) as count
            from bookings
            WHERE (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
                (date_from <= '2023-05-15' AND date_to > '2023-05-15')
            group by room_id
        )
        select (quantity - COALESCE(count, 0)) AS rooms_left FROM rooms
        left join booked_rooms on booked_rooms.room_id = rooms.id
        where hotel_id = 1
        """
        async with async_session_maker() as session:
            booked_rooms = (
                select(
                    Bookings.room_id,
                    func.count(Bookings.room_id).label("count"),
                )
                .select_from(Bookings)
                .where(
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to,
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_from,
                        ),
                    ),
                )
                .group_by(Bookings.room_id)
                .cte("booked_rooms")
            )

            get_rooms = (
                select(
                    Rooms.__table__.columns,
                    (Rooms.price * (date_to - date_from).days).label(
                        "total_cost"
                    ),
                    (
                        Rooms.quantity
                        - func.coalesce(booked_rooms.c.count, 0)
                    ).label("rooms_left"),
                )
                .join(
                    booked_rooms,
                    booked_rooms.c.room_id == Rooms.id,
                    isouter=True,
                )
                .where(Rooms.hotel_id == hotel_id)
            )

            rooms = await session.execute(get_rooms)
            return rooms.mappings().all()
