from telebot import TeleBot
import config
from googletrans import Translator

bot = TeleBot(token=config.BOT_TOKEN)
translator = Translator()

