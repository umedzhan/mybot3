from aiogram import Router, types, F
from app.keyboards.keyboards import keyboard_admin_panel

router = Router()

@router.message(F.text == "Admin panel")
async def admin_handler(message: types.Message):
    await message.answer(
        text="*ADMIN PANEL*",
        parse_mode='markdown',
        reply_markup=keyboard_admin_panel
    )
