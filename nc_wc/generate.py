from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import re

def wordcloudplot(txt):
    path = '../jieba/msyh.ttc'
    # path = unicode(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open('../jieba/背景图片库/guitar1.jpeg'))
    wordcloud = WordCloud(font_path=path, background_color="white", scale = 4,margin=5, width=1200, height=1594, mask=alice_mask, max_words=4000, max_font_size=70, random_state=42) # 可通过修改scale改变图片精度，数字越大精度越大
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('./output.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def main():
    a = []
    f = open(r'lrc.txt', 'rb').read() # 如果要分析一首歌，生成one_lrc后修改此处
    f = f.strip()
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' # 剔除标点符号
    #f = re.sub(r,'',f)

    b = ['作词','作曲','coldplay','Coldplay'] # 这里以coldplay为例,因为歌词可能会包含这些信息，显然我们不需要分析这些，故除去
    
    words = list(jieba.cut(f))
    for word in words:
        if len(word) > 1 and word not in b:
            a.append(word)

    txt = r' '.join(a)
    wordcloudplot(txt)

if __name__ == '__main__':
    main()
