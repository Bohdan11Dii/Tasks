import json
from bs4 import BeautifulSoup
import requests


url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'

html_contnt = requests.get(url).text


soup = BeautifulSoup(html_contnt, 'lxml')


data = []

tables = soup.find('table', class_='wikitable')


for tr in tables.find_all('tr')[1:]:
    country = tr.find_all('td')[2].text.strip()

    counter = 0

    for tr_nested in tables.find_all('tr')[1:]:
        if str(country[0]) == str(tr_nested.find_all('td')[2].text[0]):
            counter += 1

    data.append({
        "country": country,
        "full_country_name": tr.find_all('td')[3].text.strip(),
        "same_letter_count": counter,
        "words_count": len(tr.find_all('td')[3].text.strip().split(' ')),
        "flag_url": tr.find('a').get('href')
    })

json.dump(data, open('result.json', 'w'), ensure_ascii=False,  indent=2)


def get_small_name():
    while True:
        n = 193
        information = input('Виберіть цифру для наступних дій: \n'
                           '1 - Для вибору країни: '
                           '2 - Для виходу із програми: \n')
        if information == '1':
            small_name = input('Ведіть країну:\n')
            for i in range(n):
                if small_name.title() in data[i].values():
                    print(data[i])
                    break
            else:
               print('Вибачте, такої країни не існує')
        elif information == '2':
            print('Вихід із системи')
            break

get_small_name()