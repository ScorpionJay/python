# coding=UTF-8

import json
import urllib.parse
import urllib.request

import itchat

# config
self_nickname = 'Jay'
robot_flag = False
robot_apiKey = 'your tulin api key'

# wechat replay


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    global robot_flag
    if itchat.search_friends(userName=msg['FromUserName'])['NickName'] == self_nickname:
        print(msg.text)
        if msg.text == '1111':
            robot_flag = True
            itchat.send('Hello, filehelper', toUserName='filehelper')
        elif msg.text == '0000':
            robot_flag = False
        print('robot flag '+str(robot_flag))
    else:
        if robot_flag:
            try:
                response = robot(msg.text)
                print(response)
                msg.user.send(response)
            except:
                msg.user.send('problem...')
        else:
            print("don't care")


# tuling robot


def robot(msg):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    headers = {
        'Content-type': 'application/json'
    }
    values = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            }
        },
        "userInfo": {
            "apiKey": robot_apiKey,
            "userId": "1"
        }
    }
    data = json.dumps(values).encode('utf8')
    request = urllib.request.Request(url, data, headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    str = json.loads(html)['results'][0]['values']['text']
    # print(str)
    return str


itchat.auto_login(enableCmdQR=2)
itchat.run(True)
