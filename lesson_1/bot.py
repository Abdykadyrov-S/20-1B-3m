import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("Привет")

@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("Помогу чем смогу /start")


@dp.message(F.text == "Как дела?")
async def greeting(message: Message):
    await message.reply("Хорошо")

@dp.message(F.text.in_({'Привет', 'привет', 'салам'}))
async def greeting(message: Message):
    await message.answer("Привет")

@dp.message(Command("photo"))
async def photo(message: Message):
    await message.answer_photo(photo="https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg", caption="Вы выиграли")




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