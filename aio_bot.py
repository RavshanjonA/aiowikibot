import logging
from aiogram import Bot, Dispatcher, executor, types
from TOKEN import API_TOKEN as api_token
from wikisearch import search_wiki

API_TOKEN = api_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Alaykum\nMen WikiBotman\nAiogram da yozilganman")



@dp.message_handler()
async def SearchWiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        text = search_wiki(message)
        await message.answer(text)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)