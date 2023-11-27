import xlsxwriter
from services import get_card_data


def writer(data):
    # Создаем книгу
    book = xlsxwriter.Workbook("scrapingclub.xlsx")
    # Создаем лист под именем одежда
    page = book.add_worksheet("одежда")
    # Включаем жирный текст
    bold = book.add_format({"bold": True})
    # Включаем центровку
    centered_format = book.add_format({"align": "center"})
    # В указанные столбцы прописываем названия
    page.write("A1", "Название", bold)
    page.write("B1", "Цена", bold)
    page.write("C1", "Описание", bold)

    # Индекс в exel идет с нуля поэтому row мы указываем как начинать с 1 потому что 0 уже занят названиями столбцов
    row = 1
    column = 0
    # Прописываем ширину ячеек
    page.set_column("A:A", 30)
    page.set_column("B:B", 20, centered_format)
    page.set_column("C:C", 250)

    for item in data():
        page.write(row, column, item[0])  # item[0] - title
        page.write(row, column + 1, item[1])  # item[1] - price
        page.write(row, column + 2, item[2])  # item[2] - description
        row += 1

    book.close()


def main():
    writer(get_card_data)


if __name__ == "__main__":
    main()
