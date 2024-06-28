import logging
import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='bot.log', level=logging.INFO)

APY_KEY = os.getenv('APY_KEY_')

bot = telebot.TeleBot(APY_KEY)

COUNTRYS = ['Армения', 'Грузия', 'Сербия', 'Казахстан', 'Беларусь', 'Кыргызстан']

Person_Arminia = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Armenia = 'тут будет ссылка на гугл док'
Person_Georgia = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Georgia = 'тут будет ссылка на гугл док'
Person_Belarus = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Belarus = 'тут будет ссылка на гугл док'
Person_Kazahstan = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Kazahstan = 'тут будет ссылка на гугл док'
Person_Kyrgyzstan = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Kyrgyzstan = 'тут будет ссылка на гугл док'
Person_Serbia = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Serbia = 'тут будет ссылка на гугл док'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Что я умею")
    btn2 = types.KeyboardButton("Выбрать страну")
    btn3 = types.KeyboardButton("Задать вопрос")
    markup.add(btn1, btn2, btn3)
    msg_2 = bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я налоговый справочник собранный для ETG(Островок)".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(msg_2, func)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Что я умею"):
        bot.send_message(message.chat.id, text="Описание")
    elif (message.text == "Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Напиши свой вопрос в свободной форме, чем больше деталей - тем лучше ответ", reply_markup=markup)
        ask_question(message)
    elif (message.text == "Выбрать страну"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Грузия")
        btn2 = types.KeyboardButton("Армения")
        btn3 = types.KeyboardButton("Сербия")
        btn4 = types.KeyboardButton("Казахстан")
        btn5 = types.KeyboardButton("Беларусь")
        btn6 = types.KeyboardButton("Кыргызстан")
        btn7 = types.KeyboardButton("Россия")
        back = types.KeyboardButton("Вернуться в меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Выбери страну", reply_markup=markup)

    elif (message.text == "Вернуться в меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Что я умею")
        button2 = types.KeyboardButton("Выбрать страну")
        button_3 = types.KeyboardButton("Задать вопрос")
        markup.add(button1, button2, button_3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text in COUNTRYS):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt = types.KeyboardButton("Как физлицо")
        bt_1 = types.KeyboardButton("Как ИП")
        bt_2 = types.KeyboardButton("в меню")
        markup.add(bt, bt_1, bt_2)
        bot.send_message(message.chat.id, text="Выбери тип устройства", reply_markup=markup)

    elif (message.text == "Россия"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton("Рассчет по шкале 2025")
        b_1 = types.KeyboardButton("в меню")
        markup.add(b, b_1)
        bot.send_message(message.chat.id, text="Выбери, что ты хочешь сделать", reply_markup=markup)
    
    elif (message.text == "Рассчет по шкале 2025"):
        input_salary_gross(message)

    elif (message.text == 'в меню'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Что я умею")
        button2 = types.KeyboardButton("Выбрать страну")
        button3 = types.KeyboardButton("Задать вопрос")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == 'Как физлицо' and 'Армения'):
        bot.send_message(message.chat.id, text= {Person_Arminia})
    elif (message.text == 'Как ИП' and 'Армения'):
        bot.send_message(message.chat.id, text= {Individual_ent_Armenia})
    
    elif (message.text == 'Как физлицо' and 'Грузия'):
        bot.send_message(message.chat.id, text= {Person_Georgia})
    elif (message.text == 'Как ИП' and 'Грузия'):
        bot.send_message(message.chat.id, text= {Individual_ent_Georgia})
    
    elif (message.text == 'Как физлицо' and 'Баларусь'):
        bot.send_message(message.chat.id, text= {Person_Belarus})
    elif (message.text == 'Как ИП' and 'Беларусь'):
        bot.send_message(message.chat.id, text= {Individual_ent_Belarus})
    
    elif (message.text == 'Как физлицо' and 'Казахстан'):
        bot.send_message(message.chat.id, text= {Person_Kazahstan})
    elif (message.text == 'Как ИП' and 'Казахстан'):
        bot.send_message(message.chat.id, text= {Individual_ent_Kazahstan})
    
    elif (message.text == 'Как физлицо' and 'Кыргызстан'):
        bot.send_message(message.chat.id, text= {Person_Kyrgyzstan})
    elif (message.text == 'Как ИП' and 'Кыргызстан'):
        bot.send_message(message.chat.id, text= {Individual_ent_Kyrgyzstan})
    
    elif (message.text == 'Как физлицо' and 'Сербия'):
        bot.send_message(message.chat.id, text= {Person_Serbia})
    elif (message.text == 'Как ИП' and 'Сербия'):
        bot.send_message(message.chat.id, text= {Individual_ent_Serbia})


def input_salary_gross(message):
    logging.info("переход в input_sallary_gross")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Рассчет по шкале 2025':
        bot.send_message(message.chat.id, text="Введи свою зп, сумма в гросс")
        bot.register_next_step_handler(message, calculate_taxes_progress_scale)
    else:
        bot.send_message(message.chat.id, text="Выбери, что ты хочешь сделать",
                         reply_markup=markup)


def calculate_taxes_progress_scale(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Рассчет по шкале 2025':
        bot.send_message(message.chat.id, text="Введи свою зп, сумма в гросс")
        bot.register_next_step_handler(message, calculate_taxes_progress_scale)
    elif message.text == 'в меню':
        bot.send_message(message.chat.id, text="Выбери, что ты хочешь сделать",
                         reply_markup=markup)
    else:
        try:
            number = int(message.text)
            logging.info("message into int")
            bot.send_message(message.chat.id, text=f'''привет, твоя зп после налогов:
                            {number/2}''', reply_markup=markup)
            bot.send_message(message.chat.id, text="Выбери, в меню, что ты хочешь сделать дальше",
                         reply_markup=markup)
            
        except (TypeError, ValueError):
            logging.info("type error message not int")
            msg = bot.send_message(message.chat.id, "Вы ввели не число, попробуйте еще раз!")
            bot.register_next_step_handler(msg, calculate_taxes_progress_scale)


def ask_question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    question = message.text
    if question != "Вернуться в меню":
        message.text
        # заглушка:
        msg = bot.send_message(message.chat.id, text="magic happens", reply_markup=markup)
        bot.register_next_step_handler(msg, ask_question)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Что я умею")
        button2 = types.KeyboardButton("Выбрать страну")
        button_3 = types.KeyboardButton("Задать вопрос")
        markup.add(button1, button2, button_3)
        msg_4 = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg_4, func)

if __name__ == '__main__':

    bot.polling(none_stop=True)
    logging.info("бот стартовал")