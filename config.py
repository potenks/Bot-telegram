# config.py
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener el token del bot
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Obtener los IDs de chat
CHAT_IDS = {
    "CHAT_ID_1": os.getenv("CHAT_ID_1"),
    "CHAT_ID_2": os.getenv("CHAT_ID_2"),
    "CHAT_ID_3": os.getenv("CHAT_ID_3"),
    "CHAT_ID_4": os.getenv("CHAT_ID_4"),
    "CHAT_ID_5": os.getenv("CHAT_ID_5"),
    "CHAT_ID_6": os.getenv("CHAT_ID_6"),
}