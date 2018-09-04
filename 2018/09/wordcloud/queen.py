# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:27:38 2018

@author: Yi
"""

import os
os.chdir("C:/Users/Yi/Desktop/nlp/wordcloud")
 
import jieba.analyse                          # 导入结巴分词
import numpy as np                            # numpy
from wordcloud import WordCloud, STOPWORDS    # 词云工具和自带的的停用词，英文
from PIL import Image                         # 图片处理
import matplotlib.pyplot as plt

def handle(textfile, stopword):
    with open(textfile, 'r') as f:
        data = f.read()

    wordlist = jieba.analyse.extract_tags(data, topK=100)   # 分词，取前100
    wordStr = " ".join(wordlist)
    print (wordStr)

    hand = np.array(Image.open('plot/queen.jpg'))    # 打开一张图片，词语以图片形状为背景分布

    my_cloudword = WordCloud(
        # wordcloud参数配置
        width=1024,
        height=768,
        background_color = 'white',   # 背景颜色设置白色
        mask = hand,                  # 背景图片
        max_words = 100,              # 最大显示的字数
        stopwords = stopword,         # 停用词
        max_font_size = 100,           # 字体最大值
        font_path='data/SourceHanSerifK-Light.otf',  # 设置中文字体，若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        random_state=3,  # 设置有多少种随机生成状态，即有多少种配色方案
    )

    my_cloudword.generate(wordStr)          # 生成图片
    my_cloudword.to_file('plot/queen.png')    # 保存
    
    plt.axis('off')  # 是否显示x轴、y轴下标
    ax = plt.imshow(my_cloudword)  # 显示词云图
    fig = ax.figure
    fig.set_size_inches(25,20)                  # 可调节图片紧密 尺寸程度    
    plt.show()  # 显示


stopwords = open('data/stopwords.txt').read()
stopwords = set(stopwords.split('\n'))

if __name__ == '__main__':
    handle('data/yxgl.txt', stopwords)