from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional
import json

class Participants(BaseModel):
    id: str = Field(..., alias='_id', description='The ID of the participants.')
    p_name: str
    p_email: str
    p_password: str

    @validator("id")
    def validate_id(cls, value):
        if not ObjectId.is_valid(str(value)):
            raise ValueError(json.dumps({"status": False, "description": "Invalid ObjectId"}))
        return str(value)