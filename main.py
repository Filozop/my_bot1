
import requests
from bs4 import BeautifulSoup
URL = 'https://hdrezka24.cam/movies/1'

response = requests.get(URL)

soup = BeautifulSoup(response.text,'lxml')
data = soup.find('div',class_='th-item')
# a = [c.text for c in data]
link = 'https://hdrezka24.cam' + data.find('a',class_="th-in with-mask").get('href')
print(link)






