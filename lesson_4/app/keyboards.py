from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from aiogram.utils.keyboard import InlineKeyboardBuilder

start_button = [
    [KeyboardButton(text="Geeks"),KeyboardButton(text="Направления")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку")


direction_inline = [
    [InlineKeyboardButton(text="Backend", url="https://t.me/Abdykadyrov_S_N"),
     InlineKeyboardButton(text="Frontend", callback_data='front')]
]
direction_keyboard = InlineKeyboardMarkup(inline_keyboard=direction_inline)

front_inline = [
    [InlineKeyboardButton(text="HTML", url="https://t.me/Abdykadyrov_S_N")],
    [InlineKeyboardButton(text="CSS", url="https://t.me/Abdykadyrov_S_N")],
    [InlineKeyboardButton(text="JS", url="https://t.me/Abdykadyrov_S_N")]
]
front_keyboard = InlineKeyboardMarkup(inline_keyboard=front_inline)

geeks_inline = [
    [InlineKeyboardButton(text="студенты", callback_data="students")],
    [InlineKeyboardButton(text="ментора", callback_data="mentors")],
]
geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geeks_inline)

students = ["Султанов Нурмухаммед", "Омурзаков Нурбек", "Ниязалиев Султан"]
async def inline_students():
    keyboard = InlineKeyboardBuilder()
    for student in students:
        keyboard.add(InlineKeyboardButton(text=student, url="https://t.me/Abdykadyrov_S_N"))
    return keyboard.adjust(1).as_markup()
        