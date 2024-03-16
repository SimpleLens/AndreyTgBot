import asyncio
import logging
import random

from aiogram import types, Dispatcher, Bot
from aiogram.filters.command import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bd import DB

scheduler = AsyncIOScheduler()
token = "7038604038:AAGrjTQljAcs7OKlYTBiKgzqptPoGZYptdI"
logging.basicConfig(level = logging.INFO)
bot = Bot(token)
dp = Dispatcher()
db = DB()

@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
    if db.CheckUser(msg.from_user.id):
        return await bot.send_message(msg.from_user.id,"Ты уже учатсник проекта разгром")
    db.AddUser(msg)
    await msg.answer(f"Текущий вес Андрея - {round(db.GetWeight(), 3)} кг")

async def WeightFunc():
    Weight = db.GetWeight()
    addWeight = random.randint(3000, 4200) * 0.0001
    NewWeight = Weight + addWeight
    db.SwapWeight(NewWeight)
    message = f"За последний час Андрей набрал {round(addWeight,3)}кг, текущий вес составляет {round(NewWeight,3)} кг"

    if round(NewWeight) == 1488:
        message =  f"За последний час Андрей набрал {round(addWeight,3)}кг, текущий вес составляет {round(NewWeight,3)} кг\nОМГ, Андрей словить пасхалко😱🥵🥵"

    for i in db.GetUserId():
        try:
            await bot.send_message(i, message)
        except:
            print(f"Пользоваель {db.GetName(i)}-{i} заблокировал бота")
            db.DeleteUser(id)

async def main():
    scheduler.add_job(a, "interval", seconds=3600)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())