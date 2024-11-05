import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers import commands_router, documents_fsm_router, ALL_COMMANDS


async def main() -> None:
    load_dotenv()
    TOKEN = getenv("TG_BOT_TOKEN")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(commands_router)
    dp.include_router(documents_fsm_router)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(ALL_COMMANDS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
