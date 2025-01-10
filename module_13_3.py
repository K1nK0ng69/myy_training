
from aiogram import Bot, Dispatcher, executor, types
import asyncio

API_TOKEN = ""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    print("Бот запущен. Ожидаем сообщения...")
    executor.start_polling(dp, skip_updates=True)