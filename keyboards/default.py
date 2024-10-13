from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import LANGCODES


def get_weather():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(KeyboardButton(text="Get Weather"))
    return kb


def show_langs():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(text=lang) for lang in LANGCODES.keys()]
    kb.add(*buttons)
    return kb
