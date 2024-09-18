import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

class Register(StatesGroup):
    name = State()
    email = State()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}")

@dp.message(Command('register'))
async def reg_first(message: Message, state: FSMContext):
    await message.answer("Введите имя")
    await state.set_state(Register.name)

@dp.message(Register.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите почту")
    await state.set_state(Register.email)


@dp.message(Register.email)
async def reg_third(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Регистрация завершена")
    data = await state.get_data()
    name = data['name']
    email = data['email']

    await message.answer(f"""Ваши данные:
                         Имя - {name}
                         Почта - {email}""")
    await state.clear()


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