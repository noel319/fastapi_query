from fastapi import APIRouter, Query
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from app.models.user import User

router = APIRouter()

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client['your_db_name']
collection = db['your_collection_name']

@router.get("/users", response_model=List[User])
async def get_users(skip: int = 0, limit: int = 10):
    cursor = collection.find({}, {"_id": 0, "name": 1, "email": 1, "phone_number": 1})
    users = await cursor.skip(skip).limit(limit).to_list(length=limit)
    return users
