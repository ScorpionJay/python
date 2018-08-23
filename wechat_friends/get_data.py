import json

import pandas as pd


def get_city_data(path):
    friends = json.load(open(path))
    # print(friends)
    # df = pd.DataFrame(friends)
    # print(df)

    # df.loc[df['Province'] == '上海', 'City'] = '上海'
    # df.loc[df['Province'] == '北京', 'City'] = '北京'
    # df.loc[df['Province'] == '天津', 'City'] = '天津'
    # df.loc[df['Province'] == '重庆', 'City'] = '重庆'
    # df.loc[df['Province'] == '香港', 'City'] = '香港'
    # province_com = df.groupby(['City']).agg(['count'])
    # province_com.reset_index(inplace=True)
    # data_map = [(province_com['City'][i], province_com['AppAccountFlag']
    #              ['count'][i]) for i in range(0, province_com.shape[0])]
    # print(data_map)

    df = pd.DataFrame(friends)

    province_com = df.groupby(['Province']).agg(['count'])
    province_com.reset_index(inplace=True)
    data_map = [(province_com['Province'][i], province_com['AppAccountFlag']
                 ['count'][i]) for i in range(0, province_com.shape[0])]
    print(data_map)
    return data_map


def get_signature(path='friend.json'):
    friends = json.load(open(path))
    df = pd.DataFrame(friends)
    # print(df[['Signature']])
    data_map = [df['Signature'][i] for i in range(0, df[['Signature']].shape[0])]
    print(data_map)
    return ''.join(data_map).replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")

if __name__ == '__main__':
    # get_city_data('friend.json')
    get_signature()