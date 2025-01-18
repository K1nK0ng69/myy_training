from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

API_TOKEN = ""

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]
main_keyboard.add(*buttons)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=main_keyboard)


@dp.message_handler(Text(equals='Рассчитать'))
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.answer(f'Ваша дневная норма калорий: {calories:.2f} калорий.')
    except ValueError:
        await message.answer('Ошибка! Убедитесь, что ввели только числовые значения для возраста, роста и веса.')

    await state.finish()


@dp.message_handler(Text(equals='Информация'))
async def show_info(message: types.Message):
    await message.answer('Я бот, который помогает вам следить за здоровьем. Вы можете рассчитать вашу норму калорий!')


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Пожалуйста, выберите действие на клавиатуре или используйте команду /start.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
