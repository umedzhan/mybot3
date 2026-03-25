from aiogram import Router, types, Bot
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from app.keyboards.keyboards import keyboard_start, keyboard_phone_number, keyboard_courses
import os
from dotenv import load_dotenv
load_dotenv()

admin = os.getenv('ADMIN')

isAdmin = lambda x: admin == str(x)

from app.database.postgres import Register as RegisterUser, addUserInfo

from states.register import Register

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    chatId = message.chat.id
    firstName = message.chat.first_name
    RegisterUser(chat_id=chatId, first_name=firstName)
    await message.answer(f"Salom xush kelibsiz! {firstName}", reply_markup=keyboard_start(isAdmin(chatId)))

# start register
@router.message(lambda msg: msg.text == "Ro'yxatdan o'tish")
async def reg_start(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(Register.name)

# name
@router.message(Register.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingiz:", reply_markup=keyboard_phone_number)
    await state.set_state(Register.phone)

# phone
@router.message(Register.phone)
async def get_phone(message: types.Message, state: FSMContext):
    if message.contact:
        await state.update_data(phone=message.contact.phone_number)
    else: await state.update_data(phone=message.text)
    await message.answer("Yoshingiz:")
    await state.set_state(Register.age)

@router.message(Register.age)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Qaysi kursga yozilmoqchisiz:", reply_markup=keyboard_courses)
    await state.set_state(Register.course)
# age
@router.message(Register.course)
async def get_age(message: types.Message, state: FSMContext):
    data = await state.update_data(course=message.text)

    name = data["name"]
    phone = data["phone"]
    age = data["age"]
    course = data["course"]

    await message.answer(
        f"Ro'yxatdan o'tdingiz:\n"
        f"Ism: {name}\n"
        f"Tel: {phone}\n"
        f"Yosh: {age}\n"
        f"Kurs: {course}"
    )
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    bot1 = Bot(token=BOT_TOKEN)
    await bot1.send_message(
        chat_id=admin,
        text=f"Yangi foydalanuvchi:\nIsm: {name}\nTel: {phone}\nYosh: {age}\nKurs: {course}"
    )
    chatId = message.chat.id
    addUserInfo(chatId, name, phone, age, course)

