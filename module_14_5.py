from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import crud_functions as cf
from crud_functions import initiate_db, add_product
from crud_functions import add_user, is_included
import re
API_TOKEN = "7793618134:AAEZBoatVbVgILLsWQ2fUeyci1s5Ylbj2nQ"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [
    KeyboardButton(text='Рассчитать'),
    KeyboardButton(text='Информация'),
    KeyboardButton(text='Купить'),
    KeyboardButton(text='Регистрация')  # Новая кнопка
]
main_keyboard.add(*buttons)

buy_keyboard = InlineKeyboardMarkup(row_width=2)
buttons = [
    InlineKeyboardButton(text="Multivitamin", callback_data="product_buying"),
    InlineKeyboardButton(text="Аскорбиновая кислота", callback_data="product_buying"),
    InlineKeyboardButton(text="Vitamin D3", callback_data="product_buying"),
    InlineKeyboardButton(text="B-Complex", callback_data="product_buying")
]
buy_keyboard.add(*buttons)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

cf.initiate_db()
add_product("Multivitamin", "Поддержка иммунитета и здоровья костей", 100)
add_product("Аскорбиновая кислота", "Укрепление иммунитета и антиоксидантная защита", 200)
add_product("Vitamin D3", "Комплекс витаминов для общего здоровья", 300)
add_product("B-Complex", "Поддержка нервной системы и энергетического обмена", 400)



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


@dp.message_handler(Text(equals='Купить'))
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Multivitamin", "description": "Поддержка иммунитета и здоровья костей", "price": 100,
         "image": r"C:/Users/Ivan/Downloads/11.jpg"},
        {"name": "Аскорбиновая кислота", "description": "Укрепление иммунитета и антиоксидантная защита", "price": 200,
         "image": r"C:/Users/Ivan/Downloads/12.jpg"},
        {"name": "Vitamin D3", "description": "Комплекс витаминов для общего здоровья", "price": 300,
         "image": r"C:/Users/Ivan/Downloads/13.jpg"},
        {"name": "B-Complex", "description": "Поддержка нервной системы и энергетического обмена", "price": 400,
         "image": r"C:/Users/Ivan/Downloads/14.jpg"}
    ]

    for product in products:
        await message.answer_photo(photo=open(product["image"], 'rb'))
        await message.answer(
            f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]} руб.')

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_keyboard)


# Обработчик выбора продукта
@dp.callback_query_handler(lambda c: c.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(Text(equals='Регистрация'))
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text.strip()
    if not username:  # Проверка на пустой ввод
        await message.answer("Имя пользователя не может быть пустым. Введите имя:")
        return
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
        return
    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text.strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Простая проверка формата email
        await message.answer("Некорректный email. Введите корректный email:")
        return
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text.strip())
        if age <= 0:
            raise ValueError
    except ValueError:
        await message.answer("Ошибка! Введите корректный возраст (целое положительное число):")
        return

    data = await state.get_data()
    username = data['username']
    email = data['email']

    # Добавляем пользователя в базу данных
    add_user(username, email, age)

    await message.answer(f"Вы успешно зарегистрированы!\n"
                         f"Имя пользователя: {username}\n"
                         f"Email: {email}\n"
                         f"Возраст: {age}\n"
                         f"Баланс: 1000")
    await state.finish()


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Пожалуйста, выберите действие на клавиатуре или используйте команду /start.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
