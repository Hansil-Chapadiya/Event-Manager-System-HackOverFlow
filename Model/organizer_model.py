from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional
import json

class Organizer(BaseModel):
    id: str = Field(..., alias='_id', description='The ID of the organinzer.')
    o_name: str
    o_email: str
    o_password: str

    @validator("id")
    def validate_id(cls, value):
        if not ObjectId.is_valid(str(value)):
            raise ValueError(json.dumps({"status": False, "description": "Invalid ObjectId"}))
        return str(value)