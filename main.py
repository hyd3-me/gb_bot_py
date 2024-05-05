import asyncio
from aiogram import Bot, Dispatcher
import logging
from handlers import common, msg, career_choice


def get_sk():
    k = open('../scrt_key.py').readline()
    return k[0:-1]

async def main():
    # Логирование
    logging.basicConfig(level=logging.INFO)

    # Объект бота и диспетчера
    bot = Bot(token=get_sk())
    dp = Dispatcher()

    dp.include_router(common.router)
    dp.include_router(career_choice.router)
    dp.include_router(msg.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


