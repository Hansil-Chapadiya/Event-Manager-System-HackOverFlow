from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional
import json


class Event(BaseModel):
    id: str = Field(..., alias="_id", description="The ID of the event.")
    event_name: str
    canvas_image: str
    organizer_id: str
    event_description: str

    @validator("id")
    def validate_id(cls, value):
        if not ObjectId.is_valid(str(value)):
            raise ValueError(json.dumps({"status": False, "description": "Invalid ObjectId"}))
        return str(value)
