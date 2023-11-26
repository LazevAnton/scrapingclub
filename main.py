import requests, lxml
from bs4 import BeautifulSoup
from config import COOKIES, HEADERS, DETAIL_URL

def get_data():
    print('Начинаем сбор данных')
    cards_detail = []
    for page in range(1,7):
        try:
            session = requests.Session()
            responce = session.get(
                url='https://scrapingclub.com/exercise/list_basic/?page={page}',
                cookies=COOKIES,
                headers=HEADERS
            )
        except Exception as data_er:
            print(f'Что то пошло не так - {data_er}\n{responce.status_code}')
        soup = BeautifulSoup(responce.text, 'lxml')
        cards = soup.find_all('div', class_='w-full rounded border')
        for card in cards:
            title = card.find('div', class_='p-4').find('h4').find('a').text.strip()
            price = card.find('div', class_='p-4').find('h5').text.strip()
            card_url = f'{DETAIL_URL}{card.find("a").get("href").strip()}'
            cards_detail.append((title, price, card_url))
    print('Cбор данных окончен')
    with open('scrapingclub.txt', 'w', encoding='utf8') as file:
        for title, price, card_url in cards_detail:
            file.writelines(f'{"#" * 20}\nНаименование и цена:\n{title} - {price}\nurl - {DETAIL_URL}{card_url}\n')
            
def main():
    get_data()

if __name__ == '__main__':
    main()