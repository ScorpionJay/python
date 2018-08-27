# @description  room
# @date         2018-8-27

import urllib.request as request
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    req = request.Request(url, headers=headers)
    response = request.urlopen(req).read().decode('utf-8')

    soup = BeautifulSoup(response, 'html.parser')

    list = soup.select('.easyList li')
    for item in list:
        title = item.select('.easySub')[0].text
        price = item.select('em b')[0].text
        print('%s|%s' % (title, price))
        with open('room.txt', 'a') as file:
            file.write(title+'|'+price + '\n')


for i in range(1, 68):
    print('page ' + str(i))
    # all
    # url = 'https://www.xxx.com/list/p'+str(i)
    url = 'https://www.xxx.com/list/a14-p' + str(i)
    get_data(url)
