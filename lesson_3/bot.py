import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
admin_id = 1904375259


connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER,
first_name VARCHAR (20),
last_name VARCHAR (20),
is_primium BOOLEAN DEAFULT FALSE
)
""")


@dp.message(CommandStart())
async def start_bot(message: Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id}")
    users = cursor.fetchall()
    print(users)
    if users == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.is_premium))
        cursor.connection.commit()
    await message.answer("Привет")


@dp.message(Command("users"))
async def start_bot(message: Message):
    cursor.execute(f"SELECT first_name FROM users")
    users = cursor.fetchall()
    if message.from_user.id == admin_id:
        await bot.send_message(admin_id ,f"список всех пользователей: \n{users}")
    else:
        await message.reply("Недастаточно прав 😂")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")