from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.keyboards import after_start_keyboard


commands_router = Router()


@commands_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        text=
        "Выберите, что вам интересно узнать о программах дополнительного профессионального образования (ДПО):\n\n"
        "<b>🔹 Просмотр доступных программ</b>\n"
        "Узнайте о курсах и выберите подходящий для себя.\n\n"
        "<b>🔹 Рекомендации по выбору программы</b>\n"
        "Получите помощь в подборе курсов, которые будут полезны именно вам.\n\n"
        "<b>🔹 Заполнение заявления и договора</b>\n"
        "Заполните и получите готовые документы на обучение в формате Word.",
        reply_markup=after_start_keyboard()
    )


@commands_router.message(F.text.in_({"📊 Рекомендации", "📋 Просмотр программ"}))
@commands_router.message(Command("programs", "advice"))
async def not_implemented_commands_handler(message: Message) -> None:
    await message.answer("Пока не реализовано")
