def getTxt():
    txt = open('hamlet.txt', 'r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, ' ')
    return txt

hamletTxt = getTxt()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word in ['the','i','a','an','of','and', 'or','you','to','in']:
    del counts[word]

lst = list(counts.items())
lst.sort(key=lambda x:x[1], reverse= True)
dit = dict(lst)

for i in range(10):
    word,count = lst[i]
    print('{:<10}{:>4}'.format(word, count))