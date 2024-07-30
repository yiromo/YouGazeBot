from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

class Inline:
    @staticmethod
    def start_inline_keyboard():
        kb = InlineKeyboardBuilder()
        kb.add(InlineKeyboardButton(text="Help", callback_data="help"))
        kb.add(InlineKeyboardButton(text="Cancel", callback_data="cancel"))
        return kb.as_markup()

    @staticmethod
    def download_inline_keyboard():
        kb = InlineKeyboardBuilder()
        kb.add(InlineKeyboardButton(text="Confirm Download", callback_data="confirm_download"))
        kb.add(InlineKeyboardButton(text="Cancel", callback_data="cancel"))
        return kb.as_markup()
