"""
@AsynchronBot
"""

import asyncio
from bot import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
    InlineKeyboardButton("Каталог", callback_data="1"),
    InlineKeyboardButton("Информация", callback_data="information"),
    InlineKeyboardButton("Мои заказы", callback_data="3"),
    InlineKeyboardButton("Корзина", callback_data="4"))
    return markup

def gen_info_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
    InlineKeyboardButton("Доставка", callback_data="11"),
    InlineKeyboardButton("Оплата", callback_data="22"),
    InlineKeyboardButton("Меню", callback_data="33"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    if call.data == "information":
        await bot.answer_callback_query(call.id, "inf")
    elif call.data == "1":
        await bot.answer_callback_query(call.id, "1")

@bot.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, "Обязательный текст", reply_markup = gen_markup())

# Handle all other messages with content_type 'text' (content_types = ['text'])
@bot.message_handler(content_types = ["text"])
async def echo_message(message):
    await asyncio.sleep(3) # timer in seconds
    await bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    asyncio.run(bot.polling())