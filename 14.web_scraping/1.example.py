import requests
from bs4 import BeautifulSoup


data = requests.get('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(data.text, 'html.parser')
gifts = soup.select('#giftList > tr')

my_gifts = gifts[1:]

for g in my_gifts:
    tds = g.select('td')
    print(f"title: {tds[0].text.strip()}, price: {tds[2].text.strip()}")
    print(f"picture: {tds[3].img['src']}")