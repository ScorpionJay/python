# coding=utf-8

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = '''春天的风 能否吹来夏天的雨
    　　秋天的月 能否照亮冬天的雪
    　　夜空的星 能否落向晨曦的海
    　　山间的泉 能否遇上南飞的雁
    　　能否早一点 看透命运的伏线
    　　能否不轻易就深陷
    　　能否慢一点 挥霍有限的时间
    　　能否许我一个永远
    　　可能我撞了南墙才会回头吧
    　　可能我见了黄河才会死心吧
    　　可能我偏要一条路走到黑吧
    　　可能我还没遇见 那个他吧
    　　断掉的弦 能否扯破自缚的茧
    　　熄灭的火 能否烧光残留的念
    　　梦中的云 能否化作熟悉的脸
    　　前世的劫 能否换来今生的缘
    　　能否早一点 相信年少的誓言
    　　能否不轻易说再见
    　　能否慢一点 感受岁月的缱绻
    　　能否许我一次成全
    　　可能我撞了南墙才会回头吧
    　　可能我见了黄河才会死心吧
    　　可能我偏要一条路走到黑吧
    　　可能我还没遇见 那个他吧'''

cut = jieba.cut(text)
word = ','.join(cut)
mask = backgroud_Image = plt.imread('timg.jpg')
cloud = WordCloud(
    font_path="font.TTF",
    background_color='#000',
    mask=mask
)

wc = cloud.generate(word)
wc.to_file("wordle.jpg")
plt.imshow(wc)
plt.axis("off")
plt.show()
