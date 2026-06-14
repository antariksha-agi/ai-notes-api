from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Notecreate(BaseModel):
    title: str
    content: str
class Note(BaseModel):
    id: int
    title: str
    content: str
    summary : Optional[str] = None
    created_at: datetime
