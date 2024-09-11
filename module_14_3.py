from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


API = ''
bot = Bot(token = API)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton( text = 'Рассчитать')
button2 = KeyboardButton( text = 'Информация')
button3 = KeyboardButton( text = 'Купить')
kb.row(button)
kb.insert(button2)
kb.row(button3)

kb_in = InlineKeyboardMarkup(resize_keyboard=True)
button_in1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data= 'calories')
button_in2 = InlineKeyboardButton(text = 'Формулы расчета', callback_data= 'formulas'  )
kb_in.row(button_in1)
kb_in.insert(button_in2)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ],resize_keyboard= True
)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = ['Start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)


@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = kb_in)

@dp.message_handler(text = 'Информация')
async def main_menu(message):
    await message.answer('Мы милые и пушистые')
    with open('img_/cat.jpg', 'rb') as img:
        await message.answer_photo(img)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    await message.answer('Название: Продукт 1 | Описание: Уютный дом | Цена: 4000000руб')
    with open('img_/domik.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Название: Продукт 2 | Описание: бодрящий напиток | Цена: 100руб')
    with open('img_/cofe.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Название: Продукт 3 | Описание: поездка в горы | Цена: 50000руб')
    with open('img_/mountain.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Название: Продуки 4 | Описание: баскетбольный мяч | Цена: 5000руб')
    with open('img_/sport.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Что-нибудь приглянулось?', reply_markup = catalog_kb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('Calories = 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт')
    await call.answer()


@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age_text = message.text)
    await message.answer('Введите свой рост(см):')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_text = message.text)
    await message.answer('Введите свой вес(кг):')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight_text = message.text)
    data = await state.get_data()
    cal_ = 10*float(data['weight_text']) + 6.25*float(data['growth_text']) + 5*float(data['age_text']) +5
    await message.answer(f'Ваша норма калорий: {cal_}')
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)
