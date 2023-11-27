import xlsxwriter
from services import get_card_data

def writer(data):
    book = xlsxwriter.Workbook('scrapingclub.xlsx')
    page = book.add_worksheet('одежда')

    bold = book.add_format({'bold': True})

    page.write('A1', 'Название', bold)
    page.write('B1', 'Цена', bold)
    page.write('C1', 'Описание', bold)

    row = 1
    column = 1

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)

    for item in data():
        page.writerow(row, column, item[1])
        page.writerow(row, column+1, item[2])
        page.writerow(row, column+2, item[3])
        row +=1

    book.close()

writer(get_card_data)

def main():
    writer()

if __name__ =='__main__':
    main()