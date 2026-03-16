from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from states.register import Register

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Salom ro'yxatdan o'tish uchun /reg ni bosing!")

# start register
@router.message(Command("reg"))
async def reg_start(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(Register.name)

# name
@router.message(Register.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingiz:")
    await state.set_state(Register.phone)

# phone
@router.message(Register.phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Yoshingiz:")
    await state.set_state(Register.age)

# age
@router.message(Register.age)
async def get_age(message: types.Message, state: FSMContext):
    data = await state.update_data(age=message.text)

    name = data["name"]
    phone = data["phone"]
    age = data["age"]

    await message.answer(
        f"Ro'yxatdan o'tdingiz:\n"
        f"Ism: {name}\n"
        f"Tel: {phone}\n"
        f"Yosh: {age}"
    )

    await state.clear()