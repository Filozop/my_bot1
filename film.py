import requests
from bs4 import BeautifulSoup



URL = 'https://www.bing.com/search?q='

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('div',id="b_content")
link = 'https://www.bing.com/search?q=' + data.find('a',target= '_blank').get('href')

print(link)