from pydantic import BaseModel
from typing import Dict, Any, Optional, List
class User(BaseModel):
    full_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]  # Make this optional if it can be None
    source_data: Optional[List[Dict[str, Any]]] = None  #
def convert_objectid_to_str(user):
    user['_id'] = str(user['_id'])  # Convert _id to string
    if 'source_data' in user:
        for entry in user['source_data']:
            entry['id'] = str(entry['id'])  # Convert each source_data id to string
    return user