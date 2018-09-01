# @description  room
# @date         2018-8-27

import re
import urllib.request as request

from bs4 import BeautifulSoup

# qk


def get_qk(i):
    # url = 'https://www.qk365.com/list/p'+str(i)
    url = 'https://www.qk365.com/list/a14-p' + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    req = request.Request(url, headers=headers)
    response = request.urlopen(req).read().decode('utf-8')

    soup = BeautifulSoup(response, 'html.parser')

    list = soup.select('.easyList li')
    for item in list:
        title = item.select('.easySub')[0].text
        area = re.match('【(.*?)】',title).group(1).strip().replace('新区','').replace('区','')
        price = item.select('em b')[0].text
        print('%s|%s|%s' % (area,title, price))
        with open('room.txt', 'a') as file:
            file.write(area+'|'+title+'|'+price + '\n')

# beike


def get_bk(i):
    url = 'https://sh.zu.ke.com/zufang/pg'+str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    req = request.Request(url, headers=headers)
    response = request.urlopen(req).read().decode('utf-8')

    soup = BeautifulSoup(response, 'html.parser')

    list = soup.select('.content__list .content__list--item')
    for item in list:
        title = item.select('.content__list--item--title a')[0].text
        price = item.select('.content__list--item-price em')[0].text
        print('%s|%s' % (title, price))
        with open('room.txt', 'a') as file:
            file.write(title+'|'+price + '\n')


def main():
    get_qk(1000)
    return
    for i in range(1, 100):
        print('page ' + str(i))
        # get_bk(i)
        get_qk(i)


if __name__ == '__main__':
    main()
