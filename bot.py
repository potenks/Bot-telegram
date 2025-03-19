import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper import get_followers
from datetime import datetime

TOKEN = "7605062146:AAFyKbR1p3o7pih9jpeP51MnQ-ho8lxmhJA"
michat = "5317310399"
DE="1374599344"
Ya="216946287"
AC=""
DR="5596596568"
AP="120528488"

bot = Bot(token=TOKEN)
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
          case 1:
             mensajeoexactas +="\n"+ messageparcial
          case 2:
               mensajeoinge +="\n"+ messageparcial
          case 3:
            mensajeobser +="\n"+ messageparcial
          case 4:
            mensajeGraduados+= "\n" +messageparcial

    await bot.send_message(michat, message)
#    await bot.send_message(AP, mensajeobser)
  #  await bot.send_message(DE, message)
  #  await bot.send_message(Ya, mensajeoinge)
  #  await bot.send_message(DR,mensajeinfo)



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

