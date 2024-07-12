import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email, password, status_code", [
    ("kot@pes.com", "kotopes", 200),
    ("kot@pes.com", "kotopes", 409),
    ("no-email", "kotopes", 422),
    ("empty-password@.com", "", 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/users/register",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200),
    ("anton@example.com", "anton", 200),
    ("peso@kot.com", "kotopes", 401),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/users/login",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code
