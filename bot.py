import asyncio
from aiogram import Dispatcher
from config import bot
from handlers import horoscope


async def main():
    dp = Dispatcher()
    dp.include_router(horoscope.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
