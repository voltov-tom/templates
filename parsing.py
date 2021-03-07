import csv

import requests
from bs4 import BeautifulSoup

CSV = 'goods_ketosha.csv'
HOST = 'https://xn--80ajort1b.xn--p1ai/'
URL = 'https://xn--80ajort1b.xn--p1ai/catalog'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/'
              'webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}


def save_doc(items, path):
    with open(path, 'w', newline='\n') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Название категории', 'Ссылка на категорию', 'Изображение категории'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['goods_image']])


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_cotent(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-categories-item-slim')
    some_goods = []
    for item in items:
        some_goods.append(
            {
                'title': item.find('a').get_text(),
                'link_product': item.find('a').get('href'),
                'goods_image': item.find('figure').find('a').find('img').get('src')
            }
        )
    return some_goods


# def parser():
#     pagenation = input('Количество страниц для парсинга: ')
#     pagenation = int(pagenation.strip())
#     html = get_html(url)
#     if html.status_code == 200:
#         goods = []
#         for page in range(1, pagenation):
#             print(f'Парсинг страницы: {page}')
#             html = get_html(url, params={'page': page})
#             print(goods.extend(get_cotent(html.text)))
#     else:
#         print('error')
#
#
# parser()
html = get_html(URL)
save_doc(get_cotent(html.text), CSV)
print('Спаршено!')
