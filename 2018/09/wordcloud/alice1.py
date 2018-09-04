# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 17:53:03 2018

@author: Yi
"""

import os
os.chdir("C:/Users/Yi/Desktop/nlp/wordcloud")

from wordcloud import WordCloud

f = open('data/alice.txt').read()
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f) 
# width,height,margin可以设置图片属性
# generate 可以对全部文本进行自动分词,但是对中文支持不好
# wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
# 你可以通过font_path参数来设置字体集
#background_color参数为设置背景颜色,默认颜色为黑色

import matplotlib.pyplot as plt
ax = plt.imshow(wordcloud)
fig = ax.figure
fig.set_size_inches(25,20)    # 可调节图片紧密 尺寸程度
plt.axis("off")
plt.show()

wordcloud.to_file('plot/test.png')