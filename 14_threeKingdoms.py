# 中文分词第三方库
import jieba

txt = open('threekingdoms.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
excludes = {'将军', '却说', '二人', '不可', '荆州', '不能',
            '如此', '商议', '如何', '主公', '军士', '左右',
            '军马', '引兵', '次日', '大喜', '天下', '东吴',
            '于是', '今日', '不敢', '魏兵', '陛下', '一人',
            '都督', '人马', '不知', '汉中', '只见', '众将'}
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == '丞相' or word == '孟德':
        rword = '曹操'
    elif word == '孔明' or word == '孔明曰':
        rword = '诸葛亮'
    elif word == '关公' or word == '云长':
        rword = '关羽'
    elif word == '玄德' or word == '玄德曰':
        rword = '刘备'
    elif word == '赵子龙':
        rword = '赵云'
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

for word in excludes:
    del counts[word]

counts = list(counts.items())
counts.sort(key=lambda x:x[1], reverse=True)

for i in range(20):
    word, count = counts[i]
    print('{:<10}{:>4}'.format(word, count))