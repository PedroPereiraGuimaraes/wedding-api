from fastapi import APIRouter, HTTPException, status
from models.guest import *
from database.repositories.guest import GuestDAO

router = APIRouter()

guestDAO = GuestDAO()

@router.post('/create', status_code=status.HTTP_201_CREATED, response_description='Create a new guest', response_model=Guest)
async def create(guest: Guest):
    response = guestDAO.create(guest)
    if not response:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create guest")
    return response

@router.get('/get/{token}', response_description='Get guest info by token', response_model=Guest)
async def get(token: str):
    response = guestDAO.get(token)
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token not exists")
    return response

@router.put('/update', response_description='Update guest info by token')
async def update(guest: Guest):
    response = guestDAO.update(guest)
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token not exists")
    return response

@router.get('/confirmed', response_description='Count confirmed guests')
async def confirmed():
    response = guestDAO.get_confirmed()
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token not exists")
    return response