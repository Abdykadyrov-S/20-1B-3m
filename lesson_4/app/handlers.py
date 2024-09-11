from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router

from app.keyboards import *

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("Привет", reply_markup=start_keyboard)


@router.message(F.text == "Geeks")
async def greeting(message: Message):
    await message.reply("Информация про Geeks", reply_markup=geeks_keyboard)

@router.message(F.text == "Направления")
async def dir(message: Message):
    await message.reply("Наши основные направления:", reply_markup=direction_keyboard)

@router.callback_query(F.data == 'front')
async def inline_front(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление Frontend")
    await callback.message.edit_text("Frontend", reply_markup=front_keyboard)

@router.callback_query(F.data == 'students')
async def inline_front(callback: CallbackQuery):
    # await callback.message.answer("Frontend")
    await callback.message.edit_text("Наши студенты", reply_markup=await inline_students())

@router.message()
async def echo(message: Message):
    await message.answer(message.text)

