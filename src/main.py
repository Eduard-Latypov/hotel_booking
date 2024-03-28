import uvicorn
from fastapi import Depends, FastAPI, Query

from src.bookings.routers import router as router_booking
from src.users.router import router as router_register

app = FastAPI()

app.include_router(router_register)
app.include_router(router_booking)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
