import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper import get_followers
from datetime import datetime
from config import TELEGRAM_BOT_TOKEN, CHAT_IDS



bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

cuentas = [
    ["byte.info.unlp", "fminformaticaunlp", "lafuenteunlp", "ulla.unlp.info"],  # Informática
    ["suma_exactas", "colectivoexactas","franjaexactasunlp","gradiente.exactas"],  # Exactas
    ["cinetica_ing","franjaingenieriaunlp","listaunidad","gradienteingenieriaunlp","ulla.unlp.inge","dni.ingenieria"],  # Ingeniería
    ["suma_obser_unlp","franjamoradaobservatorio","latitud.fcag"],  # Observatorio
    ["exactasalfrente","diex.exactas"]
]
agrupaciones = ["Informática", "Exactas", "Ingeniería", "Observatorio","Graduados"]

async def send_followers():
    hoy= datetime.now().strftime("%D/%M/%Y")
    message = "📊 Seguidores de Instagram "+ hoy + ":\n\n"
    mensajeobser="📊 Observatorio " + hoy +" "
    mensajeinfo="📊 Informatica " + hoy + " "
    mensajeoinge="📊 Ingenieria " + hoy + " "
    mensajeoexactas="📊 Exactas " + hoy + " "
    mensajeGraduados= "📊 Exactas graduados " + hoy + " "
   
    for i in range(len(agrupaciones)):  # Iterar por cada grupo
        message += f"🔹 {agrupaciones[i]}\n"
        messageparcial=""
        for cuenta in cuentas[i]:  # Recorrer las cuentas del grupo
            followers = get_followers(cuenta)
            messageparcial += f"📌 {cuenta}: {followers} seguidores\n"
        message += messageparcial      
        message += "\n"  # Espacio entre agrupaciones
      
        match i:
          case 0:
             mensajeinfo +="\n"+ messageparcial 
             break
          case 1:
             mensajeoexactas +="\n"+ messageparcial
             break
          case 2:
               mensajeoinge +="\n"+ messageparcial
               break
          case 3:
            mensajeobser +="\n"+ messageparcial
            break
          case 4:
            mensajeGraduados+= "\n" +messageparcial
            break
        await bot.send_message(CHAT_IDS["CHAT_ID_1"], message)
        await bot.send_message(CHAT_IDS["CHAT_ID_2"], message)
        await bot.send_message(CHAT_IDS["CHAT_ID_3"], mensajeoinge)
        await bot.send_message(CHAT_IDS["CHAT_ID_4"], mensajeobser)
        await bot.send_message(CHAT_IDS["CHAT_ID_5"], mensajeinfo)
        await bot.send_message(CHAT_IDS["CHAT_ID_6"], mensajeGraduados)


@dp.message(Command("Mueva"))
async def manual_followers(message: Message):
    await message.reply("Procesando... ⏳")
    await send_followers()

@dp.message(Command("Seguidores"))
async def manual_followers(message: Message):
    await message.reply("Chat establecido, el que lee esto es gay")
    

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Escuchando")
    asyncio.run(main())

