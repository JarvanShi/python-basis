# 原始数据
sentence1st = 'We are the champion'
sentence2nd = 'to be or not to be'
sentence3rd = ['to','be','or','not','to','be']
lst_1 = [1,2,3,4,5,6]
lst_2 = [7,8,9]
lst_3 = [[1,2],1,1,[2,1,[1,2]]]

lst_1.extend(lst_2)
print(lst_1)

lst_1.insert(0,'number')
print(lst_1)

lst_1.pop(0)
print(lst_1)

print(sentence1st.count('be'))
print(lst_3.count(1))
print(lst_3.count([1,2]))

lst_2.extend(lst_3)
print(lst_2)

sentence3rd.remove('be')
print(sentence3rd)

lst_1.reverse()
print(lst_1)

lst_1.sort()
print(lst_1)

# 字符串方法 replace
name = 'I\'m a good boy !'
print(name)
name2 = name.replace('good','bad')
print(name2)
print(type(name))

# 列表遍历
info = {'name':'xiaowang','sex':'m','high':'175','weight':'65'}
print(info['name'])
info.get('age',18)
print(info.keys())
info['age'] = 18
print(info.keys())
print(info.values())
# info.clear()
# print(info)
# del info['age']
# print(info)
# 遍历
for key,value in info.items() :
    print(key,value)
# 枚举 enumerate
for i,key in enumerate(info.keys()) :
    print(i,key)