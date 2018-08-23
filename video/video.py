# coding=utf-8

import json
import re
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

base_url = 'please set base url'

def init(url=base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("div[id^='video_'] p a")
    for item in items:
        find(base_url+item['href'])

    print('bingo-----------------------------')


def find(url):
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    link = re.match(".*html5player.setVideoUrlHigh\('(.*?)'.*", html, re.DOTALL)
    title = re.match(".*html5player.setVideoTitle\('(.*?)'.*", html, re.DOTALL)
    if title:
        print(title.group(1))
    if link:
        print(link.group(1))


def download(path, url):
    print(path, url)
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read()
    f = open(path + '.mp4', 'ab')
    f.write(html)
    f.close()


if __name__ == '__main__':
    init()
