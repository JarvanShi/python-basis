import requests
import jieba
import wordcloud
from scipy.misc import imread

r = requests.get('https://www.python123.io/resources/pye/新时代中国特色社会主义.txt')
words = jieba.lcut(r.text) #jieba库返回值是列表
txt = ' '.join(words)

mask = imread('chinamap.jpg')
w = wordcloud.WordCloud(font_path='msyh.ttc',mask=mask ,width=800,height=600,background_color='white')
w.generate(txt) #词云库的txt文件数据要以空格分隔开
w.to_file('NewEra.jpg')
