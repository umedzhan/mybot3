from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def keyboard_start(isAdmin = False):
    keyboard = [
        [KeyboardButton(text="Ro'yxatdan o'tish")]
    ]
    if isAdmin: keyboard.append([KeyboardButton(text="Admin panel")])
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

keyboard_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

keyboard_courses = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="FrontEnd"), KeyboardButton(text="BackEnd")],
        [KeyboardButton(text="Kiber xavfsizlik")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)