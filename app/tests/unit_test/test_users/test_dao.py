from app.users.dao import UserDAO
import pytest


@pytest.mark.parametrize(
    "user_id, email, is_exist",
    [
        (1, "test@test.com", True),
        (2, "anton@example.com", True),
        (100, "none", False),
    ],
)
async def test_find_user_by_id(user_id, email, is_exist):
    user = await UserDAO.find_one_or_none(id=user_id)

    if is_exist:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user
