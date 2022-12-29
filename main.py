"""import telebot
from translate import Translator
bot = telebot.TeleBot('5894648667:AAEm94P80FaYrhJE_GPNoTQa7Mgy5hL2J4A')
translator = Translator(from_lang='ukrainian', to_lang='english')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user.first_name},привіт,я все перекладаю ,обери мову  з якою ви хочете перекладати")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,translator.translate(message.text))
bot.infinity_polling()"""
"""import requests
from bs4 import BeautifulSoup
URL = 'https://hdrezka24.cam/movies/1'

response = requests.get(URL)

soup = BeautifulSoup(response.text,'lxml')
data = soup.find('div',class_='th-item')
name = data.find('a',class_='title="Смотреть онлайн «Аватар: Путь воды»')#######TODO
print(name)"""






