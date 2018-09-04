# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:05:29 2018

@author: Yi
"""

import os
os.chdir("C:/Users/Yi/Desktop/nlp/wordcloud")

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Read the whole text.
text = open('data/alice.txt').read()
alice_coloring = np.array(Image.open("plot/alice_color.png"))  # 可随意更换图片
stopwords = set(STOPWORDS)
stopwords.add("said")

# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)


# 方式 1 ------------------------------------------------------------------------
# show

#fig, axes = plt.subplots(1, 3)
#axes[0].imshow(wc, interpolation="bilinear")
#axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
#
#for ax in axes:
#    ax.set_axis_off()
#    fig = ax.figure
#    fig.set_size_inches(25,20)                  # 可调节图片紧密 尺寸程度
#plt.show()


# 方式 2 ------------------------------------------------------------------------
# show
# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.axis("off")
ax = plt.imshow(wc, interpolation="bilinear")
fig = ax.figure
fig.set_size_inches(25,20)                  # 可调节图片紧密 尺寸程度
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
# 我们还可以直接在构造函数中直接给颜色
# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
plt.axis("off")
ax = plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
fig = ax.figure
fig.set_size_inches(25,20)                  # 可调节图片紧密 尺寸程度
plt.figure()


plt.axis("off")
ax = plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
fig = ax.figure
fig.set_size_inches(25,20)                  # 可调节图片紧密 尺寸程度
plt.show()