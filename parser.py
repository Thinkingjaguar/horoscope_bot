import requests
from bs4 import BeautifulSoup
from config import symbols

url = 'https://www.chita.ru/horoscope/daily/'


def get_pred(symbol: str):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'lxml')
    for_every_symbol = {}
    all_preds = bs.find('section', 'IjM3t').find_all('div', 'BDPZt KUbeq')
    for i in range(12):
        for_every_symbol[list(symbols.keys())[i]] = all_preds[i].text
    return for_every_symbol[symbol]
