# encoding uft-8

import time

# 输入URL
url = input('Please enter the URL:')

# 截取域名
main_name = url[11 : -4]

# 打印延时设置
print('系统正在打印中...3')
time.sleep(1)
print('系统正在打印中...2')
time.sleep(1)
print('系统正在打印中...1')
time.sleep(1)

print('The main_name is ' + main_name)