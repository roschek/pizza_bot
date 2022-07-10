from aiogram import types
from create_bot import dp, bot, Dispatcher


# @dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    # Ответ бота если бот добавлен
    await bot.send_message(message.from_user.id, message.text)


def register_helpers_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_send)
