"""
@AsynchronBot
"""

import asyncio
from bot import bot

@bot.message_handler(commands=['start'])
async def start_message(message):
	await bot.send_message(message.chat.id, 'Hello!')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await asyncio.sleep(60) # timer in seconds
    await bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    asyncio.run(bot.polling())