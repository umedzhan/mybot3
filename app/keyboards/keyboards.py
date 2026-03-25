from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

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

keyboard_admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Foydalanuvchilar ro'yxati", callback_data="users")],
        [InlineKeyboardButton(text="Soni", callback_data="count_users")],
        [InlineKeyboardButton(text="Foydalanuvchilar", callback_data="userss")]
    ]
)

test_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️", callback_data="back_1"),
            InlineKeyboardButton(text="➡️", callback_data="next_3")
        ]
    ]
)