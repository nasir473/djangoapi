import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://www.timeanddate.com/worldclock/india/visakhapatnam").text

soup = BeautifulSoup(html_text, 'lxml')
block = soup.find('section', class_ = 'bk-focus')
divi = block.find('div', id = 'qlook', class_ = 'bk-focus__qlook')
time = divi.find('span', id = 'ct', class_ = 'h1').text
print(time)