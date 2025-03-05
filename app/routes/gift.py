from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.gift import *
from database.repositories.gift import GiftDAO

router = APIRouter()

giftDAO = GiftDAO()

@router.post('/create', response_description='Create a new gift')
async def create(gift: Gift):
    response = giftDAO.create(gift)
    return JSONResponse(content=response, status_code=response.get("code", 201))

@router.get('/get', response_description='Fetch all gifts')
async def get():
    response = giftDAO.get()
    return JSONResponse(content=response, status_code=response.get("code", 200))