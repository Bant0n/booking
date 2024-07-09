import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as bookings_router
from app.hotels.rooms.router import router as hotels_router
from app.images.router import router as images_router
from app.pages.router import router as pages_router
from app.users.router import router as users_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(users_router)
app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(pages_router)
app.include_router(images_router)


# Подключение CORS, чтобы запросы к API могли приходить из браузера
origins = [
    # 3000 - порт, на котором работает фронтенд на React.js
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
