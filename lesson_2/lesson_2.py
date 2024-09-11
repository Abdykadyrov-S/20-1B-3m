import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


buttons = [
    [KeyboardButton(text='График работы')], [KeyboardButton(text="О нас")],
    [KeyboardButton(text='График работы'), KeyboardButton(text="О нас")]
]
keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

keyboard_builder = ReplyKeyboardBuilder()
for i in range(1,11):
    keyboard_builder.add(KeyboardButton(text=f"{i}"))
keyboard_builder.adjust(3)


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply(f"Привет {message.from_user.id}", reply_markup=keyboard)

@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("Помогу чем смогу /start")


@dp.message(F.text == "График работы")
async def greeting(message: Message):
    await message.reply("09:00 - 21:00")


@dp.message(F.text == "Как дела?")
async def greeting(message: Message):
    await message.reply("Хорошо")

@dp.message(Command("numbers"))
async def numbers(message: Message):
    
    await message.answer("Выберите число:", reply_markup=keyboard_builder.as_markup(resize_keyboard=True))

@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")


