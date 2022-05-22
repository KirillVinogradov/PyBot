'''
pyTelegramBotAPI/telebot
'''

from telebot.async_telebot import AsyncTeleBot
import asyncio

bot = AsyncTeleBot('5056335477:AAEA0auy_aUWj6BQMYN8WsxD37DqGntCHE4') # our bot is @AsynchronBot

@bot.message_handler(commands=['start'])
async def start_message(message):
	await bot.send_message(message.chat.id, 'Hello!')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await asyncio.sleep(60) # timer in seconds
    await bot.send_message(message.chat.id, message.text)

asyncio.run(bot.polling())
