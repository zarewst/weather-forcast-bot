from data.loader import bot, translator
from telebot import types
from googletrans import LANGCODES
from keyboards.default import show_langs
from func import get_weather_info


@bot.message_handler(func=lambda msg: msg.text == "Get Weather")
def show_weather_info_in_city(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Enter language:", reply_markup=show_langs())
    bot.register_next_step_handler(message, choose_lang)


def choose_lang(message: types.Message):
    chat_id = message.chat.id
    txt = "Напишите название города:"
    lang_from = "ru"
    lang_to = LANGCODES[message.text]
    translated_txt = translator.translate(txt, dest=lang_to, src=lang_from).text
    bot.send_message(chat_id, translated_txt)
    bot.register_next_step_handler(message, show_weather_info, lang_to)


def show_weather_info(message: types.Message, lang_to: str):
    chat_id = message.chat.id

    translation = translator.translate(get_weather_info(message.text), dest=lang_to, src="en").text

    bot.send_message(chat_id, translation)
