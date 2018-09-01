# encoding = utf-8

import time

# 英文月份和日期后缀
months = ['January ', 'February', 'March', 'April', 'May','June',
          'July', 'August', 'September', 'October', 'November', 'December']
day_endings = ['st', 'nd', 'rd'] + ['th'] * 17 + ['st', 'nd', 'rd'] + ['th'] * 7 + ['st']

# 输入年月日
year = input('Year:')
month = input('Month(1-12):')
day = input('Day(1-31):')

# 输入日期的数值类型由字符串转为整型
month_number = int(month)
day_number = int(day)

# 生成日期字符串
month_name = months[month_number - 1]
day_name = day + day_endings[day_number - 1]

# 打印延时设置
print('系统正在打印中...3')
time.sleep(1)
print('系统正在打印中...2')
time.sleep(1)
print('系统正在打印中...1')
time.sleep(1)

print('Today is '+ month_name + ' ' + day_name + ',' + year)