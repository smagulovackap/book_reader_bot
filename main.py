import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu

#initialize logger
logger = logging.getLogger(__name__)

#Bot configuring and run function
async def main():
	#logging configs
	logging.basicConfig(
		level=logging.INFO,
		format='%(filename)s:%(lineno)d #%(levelname)-8s '
				'[%(asctime)s] - %(name)s - %(message)s'
	)

	#bot running info to console
	logger.info('Starting bot')

	#loading config to Config var
	config: Config = load_config()

	#initializing bot and dispatcher
	bot: Bot = Bot(token=config.tg_bot.token,
	               parse_mode='HTML')
	dp: Dispatcher = Dispatcher()

	#main menu configuring
	await set_main_menu(bot)

	#registering router in dispatcher
	dp.include_router(user_handlers.router)
	dp.include_router(other_handlers.router)

	#skip accumulated updates and run polling
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())
