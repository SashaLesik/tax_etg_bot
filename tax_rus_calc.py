import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

APY_KEY = os.getenv('APY_KEY_')

bot = telebot.TeleBot(APY_KEY)


def input_salary_gross(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = bot.send_message(message.from_user.id, 'Введите 6 цифр: ', reply_markup = markup)
    bot.register_next_step_handler(number, calculate_taxes_progress_scale)
            
def calculate_taxes_progress_scale(number):
    print('привет', number.text)