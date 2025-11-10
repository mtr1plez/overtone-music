import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Загружаем переменные окружения (для локального тестирования, Render игнорирует)
load_dotenv() 

# 1. Получаем строку подключения из переменной окружения MONGO_URI.
# Это ОБЯЗАТЕЛЬНО для работы с Render/MongoDB Atlas.
# В Render вы установите эту переменную.
MONGO_URI = os.getenv("MONGO_URI", "mongodb://music-mongo:27017")

# 2. Получаем имя базы данных.
DB_NAME = os.getenv("DB_NAME", "music")

# Инициализация клиента. SSL/TLS будет включен автоматически при использовании "mongodb+srv" URI.
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Дополнительный тест для проверки, что MONGO_URI был установлен.
if MONGO_URI == "mongodb://music-mongo:27017":
    print("WARNING: Using local database URI. Ensure MONGO_URI is set in production!")