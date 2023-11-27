import requests, lxml
from bs4 import BeautifulSoup
from config import COOKIES, HEADERS, DETAIL_URL


def get_cards_url():
    print("Получаем url карт товара")
    for page in range(1, 8):
        try:
            session = requests.Session()
            responce = session.get(
                url=f"https://scrapingclub.com/exercise/list_basic/?page={page}",
                cookies=COOKIES,
                headers=HEADERS,
            )
        except Exception as data_er:
            print(f"Что то пошло не так - {data_er}\n{responce.status_code}")
        soup = BeautifulSoup(responce.text, "lxml")
        cards = soup.find_all("div", class_="w-full rounded border")
        for card in cards:
            card_url = f'{DETAIL_URL}{card.find("a").get("href").strip()}'
            yield card_url
    print("url карточек получен")


def get_card_data():
    for card in get_cards_url():
        session = requests.Session()
        req = session.get(url=card, cookies=COOKIES, headers=HEADERS)
        soup = BeautifulSoup(req.text, "lxml")
        card = soup.find("div", class_="p-6")
        title = card.find("h3", class_="card-title").text
        price = card.find("h4", class_="my-4 card-price").text
        description = card.find("p", class_="card-description").text
        yield title, price, description
