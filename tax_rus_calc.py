import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

APY_KEY = os.getenv('APY_KEY_')

bot = telebot.TeleBot(APY_KEY)


def input_salary_gross(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text != "Рассчет по шкале 2025" and message.text != "в меню":
        number = bot.send_message(message.from_user.id, 'magic ',
                                  reply_markup=markup)     
        bot.register_next_step_handler(number, calculate_taxes_progress_scale)
    else:
        bot.send_message(message.chat.id, text="Выбери, что ты хочешь сделать",
                         reply_markup=markup)
            
def calculate_taxes_progress_scale(number):
    number = number.text
    bot.send_message(number.chat.id, text=f'''привет, твоя зп после налогов:
                      {int(number)/2}''')