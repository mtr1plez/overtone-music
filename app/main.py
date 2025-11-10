from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from app.routes.artists import router as artist_router
from app.routes.tracks import router as track_router
from app.database import client as db_client # Импортируем клиент для проверки

app = FastAPI(title="Overtone Music Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(artist_router, prefix="/artists", tags=["artists"])
app.include_router(track_router, prefix="/tracks", tags=["tracks"])

@app.get("/")
async def root():
    """Базовый эндпоинт для проверки статуса сервиса."""
    return {"status": "ok", "message": "Overtone Music Service is running"}

@app.get("/health/db")
async def db_health_check():
    """
    Обязательный эндпоинт для проверки подключения к MongoDB Atlas.
    Пытается выполнить простую команду ping.
    """
    try:
        # Пробуем выполнить команду ping, чтобы проверить соединение
        await db_client.admin.command('ping')
        return {"status": "ok", "message": "Database connection successful"}
    except Exception as e:
        # Если не удалось подключиться, выбрасываем ошибку 500
        print(f"Database connection failed: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {e.__class__.__name__}"
        )