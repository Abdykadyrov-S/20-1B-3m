import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


bot = Bot(token="TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("Привет")

@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("Помогу чем смогу /start")




"""
/start - начать бот, если пользователь начал пользоватся с ботом то его мы
должны записать в базу (id пользователя , имя пользователя,id чата,
is_admin является ли пользователь админом по умолчания false, если true
то пользователь будет админом)

Reply кнопки после нажатия на start (для админов)
mailing - рассылка. То есть нужно сделать рассылку сообщения для всех
пользователей бота 
users - узнать всех пользователей бота 

Inline кнопка на сообщение после пользователей
Добавить админа - добавить админа 
удалить админа - удалить админа 


"""


@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")