from pydantic import BaseModel
from typing import Optional

class Artist(BaseModel):
    name: str
    country: Optional[str] = None
    genre: Optional[str] = None

class Track(BaseModel):
    title: str
    artist_id: str
    album: Optional[str] = None
    year: Optional[int] = None
    cover_url: Optional[str] = None
