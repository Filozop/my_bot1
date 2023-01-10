import requests
from bs4 import BeautifulSoup
import telebot

TOKEN = '5740820565:AAF_P7ZoRpiQYFUQ3WbKYJRC5HE_r4QyMD4'
bot = telebot.TeleBot(TOKEN)

for number in range(1,2698):

    URL = f'https://hdrezka24.cam/movies/1{number}'

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='th-item')
    for i in data:
        name = i.find('a', class_='th-in with-mask').get('title').replace("Смотреть онлайн ","")
        year = i.find('div',class_='th-year').text
        quality = i.find('div',class_="th-series").text
        # a = [c.text for c in data]
        link = 'https://hdrezka24.cam' + i.find('a', class_="th-in with-mask").get('href')

        with open('films.txt','a',encoding='utf-8') as file:
            file.write('\n' + name + ',' + year + ',' + quality + ',' + link)


        def search_film(name):
            with open('films.txt', 'r', encoding='utf-8') as file:
                for i in file.readlines():
                    if name in i:
                        return i.split(',')


# @bot.message_handler(commands=['start'])
# def welcome_user(message):
#     bot.reply_to(message,
#                  f"{message.from_user.first_name},привіт!,\nВведи назву фільму ,який хочете подивитися:")
#     bot.register_next_step_handler(message,search_film)
#
# @bot.message_handler(func=lambda message: True)
# def search_film(message):
#     if message.text == name(URL):
#         bot.reply_to(message,f"{message.from_user.first_name},Фільм знайдено,\n приємного перегляду)
#     else:
#         bot.register_next_step_handler(message,error)
#
# def error(message):
#     bot.reply_to(message,f"{message.from_user.first_name} Переконайтеся, що ввели правильну назву фільму")
#     bot.register_next_step_handler(message, search_film)
#
# bot.infinity_polling()