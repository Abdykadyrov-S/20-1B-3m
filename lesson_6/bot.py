import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from bs4 import BeautifulSoup
import requests

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}")

@dp.message(Command("parsing"))
async def start(message: Message):
    response = requests.get(url="https://www.nbkr.kg/index.jsp?lang=RUS")
    soup = BeautifulSoup(response.text, 'lxml')

    course = soup.find_all('table', class_="table table-striped")
    for title in course:
        print(f"{title.text}")
        await message.answer(title.text)


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