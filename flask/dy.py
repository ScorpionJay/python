# kuaiyinshi video
# date 2018-8-24

import json
import re
import urllib.request

from flask import Flask, render_template
from flask_cors import CORS


def get_data(url='https://kuaiyinshi.com/api/dou-yin/recommend'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    items = json.loads(html)['data']

    for item in items:
        print(item['nickname'])
        video_url = item['video_url']
        matchObj = re.match('.*video_id=(.*?)&', video_url)
        if matchObj:
            video_id = matchObj.group(1)
            real_video_id = decrypt(video_id)
            new_video_url = video_url.replace(video_id, real_video_id)

            if(new_video_url.find('api.amemv.com/aweme/') > -1):
                new_video_url = new_video_url.replace('playwm', "play")

            print(new_video_url)
            item['video_url'] = new_video_url

    return items


def decrypt(s, key=[65, 48, 77, 106, 90, 102, 77, 84, 89, 48, 78, 68, 65, 51, 77, 106]):
    arr = s.split(':')
    # keys = [ord(i) for i in "A0MjZfMTY0NDA3Mj"]
    e = ''
    for i in range(len(arr)):
        if i != 0:
            v = chr(int(arr[i]) - (255 & key[(i-1) % len(key)]))
            e += v
    return e


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/")
def index():
    return render_template('index.html', contents='This is index page')


@app.route("/video")
def video():
    return json.dumps(get_data())


if __name__ == "__main__":
    app.run(port=8889)
