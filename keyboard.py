from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import symbols


def what_is_your_horoscope_symbol():
    kb = InlineKeyboardBuilder()
    for call_data, text in symbols.items():
        kb.button(text=text, callback_data=call_data)
    kb.adjust(2)
    return kb.as_markup()
