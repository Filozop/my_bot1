import requests
from bs4 import BeautifulSoup
from time import sleep
import telebot

TOKEN = '5740820565:AAF_P7ZoRpiQYFUQ3WbKYJRC5HE_r4QyMD4'
bot = telebot.TeleBot(TOKEN)

for number in range(1,2698):
    sleep(2)
    URL = f'https://hdrezka24.cam/movies/1{number}'

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='th-item')
    for i in data:
        name = i.find('a', class_='th-in with-mask').get('title')
        year = i.find('div',class_='th-year').text
        # a = [c.text for c in data]
        link = 'https://hdrezka24.cam' + i.find('a', class_="th-in with-mask").get('href')
        print(name + '\n' + year +'года' + '\n' + link)
@bot.message_handler(commands=['start'])
def a(massage):











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






