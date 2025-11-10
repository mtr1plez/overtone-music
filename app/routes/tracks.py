from fastapi import APIRouter, HTTPException
from app.models import Track
from app.database import db
from bson import ObjectId

router = APIRouter()
tracks_collection = db["tracks"]
artists_collection = db["artists"]  # ✅ Добавлено

def fix_id(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/")
async def create_track(track: Track):
    result = await tracks_collection.insert_one(track.dict())
    created = await tracks_collection.find_one({"_id": result.inserted_id})
    return fix_id(created)

@router.get("/")
async def get_tracks():
    items = await tracks_collection.find().to_list(100)
    for item in items:
        artist = await artists_collection.find_one({"_id": ObjectId(item["artist_id"])})
        item["artist_name"] = artist["name"] if artist else "Unknown Artist"
    return [fix_id(i) for i in items]

@router.get("/{track_id}")
async def get_track(track_id: str):
    track = await tracks_collection.find_one({"_id": ObjectId(track_id)})
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    # ✅ Достаём связанного артиста по artist_id
    artist = await artists_collection.find_one({"_id": ObjectId(track["artist_id"])})

    # ✅ Добавляем artist_name в ответ
    track["artist_name"] = artist["name"] if artist else "Unknown Artist"

    return fix_id(track)
