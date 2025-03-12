from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import guest, gift

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(guest.router, prefix="/guest", tags=["guest"])
app.include_router(gift.router, prefix="/gift", tags=["gift"])