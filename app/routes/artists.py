from fastapi import APIRouter
from app.models import Artist
from app.database import db
from bson import ObjectId

router = APIRouter()
collection = db["artists"]

def fix_id(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/")
async def create_artist(artist: Artist):
    result = await collection.insert_one(artist.dict())
    created = await collection.find_one({"_id": result.inserted_id})
    return fix_id(created)

@router.get("/")
async def get_artists():
    items = await collection.find().to_list(100)
    return [fix_id(i) for i in items]
