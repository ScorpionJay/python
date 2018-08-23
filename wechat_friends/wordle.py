from get_data import get_signature

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = get_signature()

cut = jieba.cut(text)
word = ','.join(cut)
mask = backgroud_Image = plt.imread('timg.jpg')
cloud = WordCloud(
    font_path="font.TTF",
    background_color='#000',
    mask=mask,
    # scale=2,
    # min_font_size=5
)

wc = cloud.generate(word)
wc.to_file("wordle.jpg")
plt.imshow(wc)
plt.axis("off")
plt.show()
