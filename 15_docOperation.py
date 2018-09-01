txt = open('test_1.txt', 'x+')
lst = [['姓名', '学号', '班级', '年龄'],
       ['张三', '10086', '金融1班', '18']]

# 写入文件
for item in lst:
    txt.write(','.join((item)) + '\n')
print('========分隔符========')

# 一次读取，分行处理
txt.seek(0)
for line in txt.readlines():
    line = line.replace('\n', '')
    print(line)
print('========分隔符========')

# 分行读取，分行处理
txt.seek(0)
for line in txt:
    line = line.replace('\n', '')
    print(line)
print('========分隔符========')

# 读取文件
txt.seek(0)
ls = []
for line in txt:
    line = line.replace('\n', '')
    ls.append(line.split(','))

# 遍历二维文件
for row in ls:
    for column in row:
        print(column, end=' ')
    print('\n')

txt.close()