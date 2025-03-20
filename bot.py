# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper import get_followers
from datetime import datetime
from config import TELEGRAM_BOT_TOKEN, CHAT_IDS, AGRUPACIONES, CUENTAS

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

async def send_followers():
    hoy = datetime.now().strftime("%d/%m/%Y")
    message = f"📊 Seguidores de Instagram ({hoy}):\n\n"
    mensajes_personalizados = {
        "CHAT_ID_3": f"📊 Ingeniería {hoy}\n",
        "CHAT_ID_4": f"📊 Observatorio {hoy}\n",
        "CHAT_ID_5": f"📊 Informática {hoy}\n",
        "CHAT_ID_6": f"📊 Exactas graduados {hoy}\n",
    }

    for i, agrupacion in enumerate(AGRUPACIONES):  # Iterar por cada grupo
        message += f"🔹 {agrupacion}\n"
        messageparcial = ""
        for cuenta in CUENTAS[i]:  # Recorrer las cuentas del grupo
            try:
                followers = get_followers(cuenta)
                messageparcial += f"📌 {cuenta}: {followers} seguidores\n"
                print(cuenta + " ready")
            except Exception as e:
                messageparcial += f"📌 {cuenta}: Error al obtener seguidores ({str(e)})\n"
                print(cuenta + " error")
        message += messageparcial
        message += "\n"  # Espacio entre agrupaciones

        # Agregar el mensaje parcial al mensaje personalizado correspondiente
        match i:
            case 0:
                mensajes_personalizados["CHAT_ID_5"] += messageparcial
            case 1:
                mensajes_personalizados["CHAT_ID_6"] += messageparcial
            case 2:
                mensajes_personalizados["CHAT_ID_3"] += messageparcial
            case 3:
                mensajes_personalizados["CHAT_ID_4"] += messageparcial

    # Enviar mensajes a los chats correspondientes
    await bot.send_message(CHAT_IDS["CHAT_ID_1"], message)
    await bot.send_message(CHAT_IDS["CHAT_ID_2"], message)
    for chat_id_key, mensaje in mensajes_personalizados.items():
        await bot.send_message(CHAT_IDS[chat_id_key], mensaje)

@dp.message(Command("/"))
async def manual_followers(message: Message):
    await message.reply("Procesando... ⏳")
    await send_followers()

@dp.message(Command("/8"))
async def set_chat(message: Message):
    await message.reply("Chat establecido. ¡Listo para recibir actualizaciones!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    print("Escuchando...")
    asyncio.run(main())