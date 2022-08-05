import json
import string
from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def delete_mat(message: types.message):
    cenzure_set = {i.lower().replace(string.punctuation, '') for i in message.text.split()}
    with open('mat.json', 'rb') as f:
        if cenzure_set.intersection(set(json.load(f))) != set():
            await message.reply('Маты запрещены')
            await message.delete()
        

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(delete_mat)
    