from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await  message.delete()
    except:
        await message.reply('Общение с ботом через лс. напишите ему: \nhhtps://t.me/roschekPizzaBot')


# @dp.message_handler(commands=['Режим_работы'])
async def open__command(message: types.message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9.00 - 19.00; Сб-Вс с 11.00 до 17.00')


# @dp.message_handler(commands=['Расположение'])
async def place__command(message: types.message):
    await bot.send_message(message.from_user.id, 'СПб, Невский пр. 132')


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open__command, commands=['Режим_работы'])
    dp.register_message_handler(place__command, commands=['Расположение'])
