import jieba
import wordcloud
from scipy.misc import imread

f = open('threekingdoms.txt','r',encoding='utf-8').read()
txt = jieba.lcut(f,cut_all=True)
words = ' '.join(txt)

mask = imread('chinamap.jpg')
w = wordcloud.WordCloud(font_path='msyh.ttc',width=800,height=600,mask=mask,background_color='white')
w.generate(words)
w.to_file('threekingdoms.jpg')