from aiogram.utils import executor
from create_bot import dp

async def on_startup(_):
    print('Bot is online')

from handlers import client, admin, helpers

client.register_client_handlers(dp)
helpers.register_helpers_handlers(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)