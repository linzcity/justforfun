from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

def wordcloudplot(txt):
    path = 'E:/jieba/msyh.ttc' # 字体路径 ，路径都为绝对路径
    # path = unicode(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open('E:/jieba/背景图片库/qishi.jpeg')) # 背景图片路径，注意只有不透明部分会填充
    wordcloud = WordCloud(font_path=path, background_color="white", scale = 2,margin=5, width=1200, height=1594, mask=alice_mask, max_words=4000, max_font_size=80, random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('E:/output.jpg') # 生成图片位置
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def main():
    a = []
    f = open(r'E:\output.txt', 'rb').read() # 文档位置
    words = list(jieba.cut(f))
    for word in words:
        if len(word) > 1:
            a.append(word)
    txt = r' '.join(a)
    wordcloudplot(txt)

if __name__ == '__main__':
    main()
