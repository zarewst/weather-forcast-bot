from data.loader import bot
from telebot import types
from keyboards.default import get_weather


@bot.message_handler(commands=["start"])
def start_command(message: types.Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name

    bot.send_message(chat_id, f"Hi {full_name}!", reply_markup=get_weather())


# @bot.messsage_handler(func=lambda msg: msg == "/help")
# def help_command(message: types.Message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, "This bot shows the forecast of the certain city")
