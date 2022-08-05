from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Продукты', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/SpecificProductsBot')

# @dp.message_handler(commands=['Расположение'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'На каникулах')

async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Глобус')

async def what_buy(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])    
    dp.register_message_handler(place_command, commands=['Расположение'])    
    dp.register_message_handler(what_buy, commands=['Что_купить'])    
