from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.guest import *
from database.repositories.guest import GuestDAO

router = APIRouter()

guestDAO = GuestDAO()

@router.post('/create', response_description='Create a new guest')
async def create(guest: Guest):
    response, status_code = guestDAO.create(guest)
    return JSONResponse(content=response, status_code=status_code)

@router.get('/get/{token}', response_description='Get guest info by token')
async def get(token: str):
    response, status_code = guestDAO.get(token)
    return JSONResponse(content=response, status_code=status_code)

@router.put('/update', response_description='Update guest info by token')
async def update(guest: Guest):
    response, status_code = guestDAO.update(guest)
    return JSONResponse(content=response, status_code=status_code)

@router.get('/confirmed', response_description='Count confirmed guests')
async def confirmed():
    response, status_code = guestDAO.get_confirmed()
    return JSONResponse(content=response, status_code=status_code)