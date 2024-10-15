from fastapi import APIRouter, Query, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Optional
import re
from app.models.user import User, convert_objectid_to_str

router = APIRouter()

# MongoDB connection
client = AsyncIOMotorClient('mongodb://twuser:moniThmaRtio@192.168.20.75:27017/admin')
meta_db = client['meta']
personal_collection = meta_db['personal']

# Email validation regex
email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def is_valid_email(email: str) -> bool:
    return bool(re.match(email_regex, email))

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
        query['full_name'] = name
    
    print("Query Name:", query)
    
    # Perform the query without projection to get all fields
    cursor = personal_collection.find(query)
    
    # Convert the cursor to a list of dictionaries
    try:
        users = await cursor.to_list(length=None)
        formatted_users = [convert_objectid_to_str(user) for user in users]
        
        # Validate emails and replace invalid ones
        for user in formatted_users:
            if 'email' in user and not is_valid_email(user['email']):
                user['email'] = "Unknown"  # Replace invalid email with a placeholder

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not formatted_users:
        raise HTTPException(status_code=404, detail="No users found.")

    return formatted_users
