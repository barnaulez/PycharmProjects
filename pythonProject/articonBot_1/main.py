from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import random
HELP_COMMAND = """
/start - Начать работу с Артиботом
/about - О боте
/help - Список команд
"""

BOT_ABOUT = """
Привет! Я - Артибот, Виртуальный помощник Учебного центра Артикон!
Сейчас я почти ничего не умею, но я учусь, и скоро смогу сделать общение с Учебным центром Артикон быстрым, удобным и выгодным!
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
count = 0

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text = HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Привет! Я - Артибот, Виртуальный помощник Учебного центра Артикон!")
    await message.delete()

@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    await message.reply(text = BOT_ABOUT)
    await message.delete()

@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global count
    await message.reply(f'COUNT: {count}')
    await message.delete()
    count += 1

@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.reply('YES')
    else:
        await message.reply('NO')
        await message.answer(text=random.choice(alphabet))
    
if __name__ == '__main__':
    executor.start_polling(dp)