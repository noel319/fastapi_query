from fastapi import APIRouter, Query
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Optional
from app.models.user import User

router = APIRouter()

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client['meta']
collection = db['personal']

@router.get("/users", response_model=List[User])
async def get_users(
    email: Optional[str] = None,
    phone_number: Optional[str] = None,
    name: Optional[str] = None
):
    # Build MongoDB query dynamically based on provided filters
    query = {}
    if email:
        query['email'] = email
    if phone_number:
        query['phone_number'] = phone_number
    if name:
        query['name'] = name
    
    # Perform the query without projection to get all fields
    cursor = collection.find(query)
    
    # Convert the cursor to a list of dictionaries
    users = await cursor.to_list(length=None)
    
    return users
