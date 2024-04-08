import asyncio
from aiogram import Bot, Dispatcher

from handlers import bot_messages, user_commands, group_commands, admin_commands, questionaire, appeal, channel
from callbacks import pagination, add_request

from middlewares.check_sub import CheckSubscription
from middlewares.throttling import ThrottlingMiddleware

from config_reader import config

async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.message.middleware(ThrottlingMiddleware(1))

    dp.include_routers(
        user_commands.router,
        admin_commands.router,
        group_commands.router,
        pagination.router,
        appeal.router,
        add_request.router,
        questionaire.router,
        channel.router,
        bot_messages.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())