from aiogram import Router, types
from aiogram import F
from app.database.postgres import getUsers, countUsers, getUser
from app.keyboards.keyboards import test_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(F.data == 'users')
async def users_query_handler(callback: types.CallbackQuery):
    users = getUsers()
    response_text = ""
    for user in users:
        response_text += f"{user[1]} {user[2]}\n"
    await callback.message.answer("Foydlanuvchilar:\n"+response_text)

@router.callback_query(F.data == 'count_users')
async def count_users_query_handler(callback: types.CallbackQuery):
    count_users = countUsers()
    await callback.message.answer(f"Foydalanuvchilar soni: {count_users}")

@router.callback_query(F.data == 'userss')
async def userss_query_handler(callback: types.CallbackQuery):
    user = getUser(0)
    count_user = countUsers()
    response_text = (f"<b>Foydalanuvchi:</b>\n\n"
                     f"<b>id:</b> {user[1]}\n"
                     f"<b>telegram nomi:</b> {user[2]}\n"
                     f"<b>F.I.SH:</b> {user[3]}\n"
                     f"<b>Telefon raqami:</b> {user[4]}\n"
                     f"<b>Yoshi:</b> {user[5]}\n"
                     f"<b>Kurs:</b> {user[6]}")
    text_count_user = f"1/{count_user}"
    await callback.message.edit_text(
        text=response_text,
        parse_mode='html',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⬅️', callback_data='page_-1'),
                    InlineKeyboardButton(text=text_count_user, callback_data='count_user'),
                    InlineKeyboardButton(text='➡️', callback_data='page_1')]
            ]
        )
    )

@router.callback_query(F.data.startswith('page_'))
async def left_user_query_handler(callback: types.CallbackQuery):
    page = int(callback.data.replace('page_', ''))
    user = getUser(page)
    count_user = countUsers()
    response_text = (f"<b>Foydalanuvchi:</b>\n\n"
                     f"<b>id:</b> {user[1]}\n"
                     f"<b>telegram nomi:</b> {user[2]}\n"
                     f"<b>F.I.SH:</b> {user[3]}\n"
                     f"<b>Telefon raqami:</b> {user[4]}\n"
                     f"<b>Yoshi:</b> {user[5]}\n"
                     f"<b>Kurs:</b> {user[6]}")
    text_count_user = f"{page+1}/{count_user}"
    await callback.message.edit_text(
        text=response_text,
        parse_mode='html',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⬅️', callback_data=f"page_{page-1}"),
                    InlineKeyboardButton(text=text_count_user, callback_data='count_user'),
                    InlineKeyboardButton(text='➡️', callback_data=f"page_{page+1}")]
            ]
        )
    )