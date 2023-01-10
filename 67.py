"""import telebot

bot = telebot.TeleBot('5919663839:AAEDAK-g0w3UnM1a9LHMlYZStcMOAlKsZow')

# b1=1
# while b1==b1:
#     s=input('')
#     if s=='не повторюй за мною':
#         print('хахахахахахахахахаха')
#     else:
#         print(s)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user.first_name}, привіт, я все повторюю")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()"""
"""def func (age):
    if age >= 18:
        return('Ви можете вживати алкогольні напої')
    else:
        return('Ви не можете вживати алкогольні напої')
age = int(input('Скільки вам років?'))
print(func(age))"""




"""import requests
# from bs4 import BeautifulSoup
# URL = 'https://www.google.com/'
#
# response = requests.get(URL)
#
# soup = BeautifulSoup(response.text,'lxml')
# data = soup.find('li',class_='b_algo')
# # a = [c.text for c in data]
# link = data.find('a',class_="target").get('href')"""