from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot is online')

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await  message.delete()
    except:
        await message.reply('Общение с ботом через лс. напишите ему: \nhhtps://t.me/roschekPizzaBot')

@dp.message_handler(commands=['Режим_работы'])
async def open__command(message: types.message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9.00 - 19.00; Сб-Вс с 11.00 до 17.00')

@dp.message_handler(commands=['Расположение'])
async def place__command(message: types.message):
    await bot.send_message(message.from_user.id, 'СПб, Невский пр. 132')


@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    # Ответ бота если бот добавлен
    await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)