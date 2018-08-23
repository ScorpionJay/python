import io
import json
import re
import sys
import time

import itchat


def login():
    itchat.auto_login(enableCmdQR=2, hotReload=True)

    itchat.send('Hello, filehelper', toUserName='filehelper')

    friends = itchat.get_friends(update=True)[0:]
    print(friends)
    json.dump(friends, open('friend.json', "w"), ensure_ascii=False)

    time.sleep(20)
    itchat.logout()


if __name__ == '__main__':
    login()
