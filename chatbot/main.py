import logging
import os
import telebot
from telebot import types
from dotenv import load_dotenv
import requests
from decimal import Decimal, getcontext

getcontext().prec = 7

load_dotenv()

#logging.basicConfig(filename='bot.log', level=logging.INFO)
logging.basicConfig(level=logging.INFO)

APY_KEY = os.getenv('APY_KEY_')

bot = telebot.TeleBot(APY_KEY)

COUNTRYS = ['Армения', 'Грузия', 'Сербия', 'Казахстан', 'Беларусь', 'Кыргызстан']

Person_Arminia = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Armenia = 'тут будет ссылка на гугл док'
Person_Georgia = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Georgia = 'тут будет ссылка на гугл док'
Person_Turkey = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Turkey = 'тут будет ссылка на гугл док'
Person_Kazahstan = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Kazahstan = 'тут будет ссылка на гугл док'
Person_Kyrgyzstan = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Kyrgyzstan = 'тут будет ссылка на гугл док'
Person_Serbia = 'тут будет ссылка на гугл док с описанием'
Individual_ent_Serbia = 'тут будет ссылка на гугл док'
DESCRIPTION = 'Тут будет описание. Для России расчеты приведены для резиентов, устроенных по ТК РФ'

def calculate_tax_2025(number):
    number = Decimal(str(number))

    if int(number*Decimal('12')) <= 2400000:
        sallary_per_month = number - number*Decimal('0.13')
        return sallary_per_month
    elif 2400000 < int(number*Decimal('12')) <= 5000000:
        sallary_per_year = number*Decimal('12') - (Decimal('312000') - (number - Decimal('2400000'))*Decimal('0.15'))
        sallary_per_month = int(sallary_per_year / Decimal('12'))
        return sallary_per_month
    elif 5000000 < int(number*Decimal('12')) <= 20000000:
        sallary_per_year = number*Decimal('12') - (Decimal('702000') - (number - Decimal('5000000'))*Decimal('0.18'))
        sallary_per_month = int(sallary_per_year / Decimal('12'))
        return sallary_per_month
    elif 20000000 < int(number*Decimal('12')) <= 50000000:
        sallary_per_year = number*Decimal('12') - (Decimal('3402000') - (number - Decimal('20000000'))*Decimal('0.20'))
        sallary_per_month = int(sallary_per_year / Decimal('12'))
        return sallary_per_month
    else:
        sallary_per_year = number*Decimal('12') - (Decimal('9402000') - (number - Decimal('50000000'))*Decimal('0.22'))
        sallary_per_month = int(sallary_per_year / Decimal('12'))
        return sallary_per_month



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
        bot.send_message(message.chat.id, text={DESCRIPTION})
    elif (message.text == "Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Напиши свой вопрос в свободной форме, чем больше деталей - тем лучше ответ", reply_markup=markup)
        bot.register_next_step_handler(message, ask_question)
    elif (message.text == "Выбрать страну"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Грузия")
        btn2 = types.KeyboardButton("Армения")
        btn3 = types.KeyboardButton("Сербия")
        btn4 = types.KeyboardButton("Казахстан")
        btn5 = types.KeyboardButton("Турция")
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
    
    elif (message.text == 'Как физлицо' and 'Турция'):
        bot.send_message(message.chat.id, text= {Person_Turkey})
    elif (message.text == 'Как ИП' and 'Беларусь'):
        bot.send_message(message.chat.id, text= {Individual_ent_Turkey})
    
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
        bot.send_message(message.chat.id, text="Введи свою зп с учетом бонусов за 1 месяц, сумма в гросс")
        bot.register_next_step_handler(message, calculate_taxes_progress_scale)
    else:
        bot.send_message(message.chat.id, text="Выбери, что ты хочешь сделать",
                         reply_markup=markup)


def calculate_taxes_progress_scale(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Рассчет по шкале 2025':
        bot.send_message(message.chat.id, text="Введи свою зп с учетом бонусов за 1 месяц, сумма в гросс")
        bot.register_next_step_handler(message, calculate_taxes_progress_scale)
    elif message.text == 'в меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Что я умею")
        button2 = types.KeyboardButton("Выбрать страну")
        button3 = types.KeyboardButton("Задать вопрос")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        try:
            number = int(message.text)
            logging.info("message into int")
            bot.send_message(message.chat.id, text=f'''привет, твоя зп после налогов (в месяц):
                            {calculate_tax_2025(number)}''', reply_markup=markup)
            # osh: мне каж можно это убрать и так понятно, что в меню надо что-то сделать
            # bot.send_message(message.chat.id, text="Выбери в меню, что ты хочешь сделать дальше",
            #                  reply_markup=markup)
            bot.register_next_step_handler(message, calculate_taxes_progress_scale)
            
        except (TypeError, ValueError):
            logging.info("type error message not int")
            msg = bot.send_message(message.chat.id, "Вы ввели не число, попробуйте еще раз!")
            bot.register_next_step_handler(msg, calculate_taxes_progress_scale)


def ask_question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    question = message.text
    if question != 'Вернуться в меню':
        try:
            data = {'query': question}
            response = requests.post('http://llm:5005/llm_query', json=data, headers={'Content-Type': 'application/json'})
            logging.info(f"response {response.json()}")
        except Exception:
            response = 'Не получилось найти информацию :('
            logging.error(f'Unsuccessful request: {response}')
        bot.send_message(message.chat.id, text=response.json()['response'], reply_markup=markup)
        msg = bot.send_message(message.chat.id, 
                               'Можешь уточнить вопрос или задать новый. Нажми "вернуться в меню" чтобы вернуться')
        bot.register_next_step_handler(msg, ask_question)
    else:
        func(message)


if __name__ == '__main__':

    bot.polling(none_stop=True)
    logging.info("бот стартовал")