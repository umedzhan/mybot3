from aiogram import Router, types
from aiogram import F
from app.database.postgres import getUsers, countUsers

router = Router()

@router.callback_query(F.data == 'users')
async def users_query_handler(callback: types.CallbackQuery):
    users = getUsers()
    response_text = ""
    for user in users:
        response_text += f"{user[1]} {user[2]}\n"
    await callback.message.answer("Foydlanuvchilar:\n   "+response_text)

@router.callback_query(F.data == 'count_users')
async def count_users_query_handler(callback: types.CallbackQuery):
    count_users = countUsers()
    await callback.message.answer(f"Foydalanuvchilar soni: {count_users}")