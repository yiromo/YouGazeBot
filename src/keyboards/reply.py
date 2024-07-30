from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

class Reply:
    @staticmethod
    def main_buttons():
        buttons = [
            [
                KeyboardButton(text="🛒 All products"),
                KeyboardButton(text="📦 Product availability"),
                KeyboardButton(text="👤 Profile"),
            ],
            [
                KeyboardButton(text="📜 Rules"),
                KeyboardButton(text="❓ Help"),
                KeyboardButton(text="ℹ️ About us"),
            ],
        ]
        keyboard_markup = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=False
        )
        return keyboard_markup

    @staticmethod
    def start_buttons():
        buttons = [
            [
                KeyboardButton(text="Start"),
            ],
        ]
        keyboard_markup = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=True
        )
        return keyboard_markup

    @staticmethod
    def help_buttons():
        buttons = [
            [
                KeyboardButton(text="Help"),
                KeyboardButton(text="Cancel"),
            ],
        ]
        keyboard_markup = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=True
        )
        return keyboard_markup

    @staticmethod
    def cancel_buttons():
        buttons = [
            [
                KeyboardButton(text="Cancel"),
            ],
        ]
        keyboard_markup = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=True
        )
        return keyboard_markup
