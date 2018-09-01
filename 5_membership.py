import time

database = [['Jarvan','123'],['David','234'],['Smith','345'],['Albert','456']]
username = input('user name:')
password = input('password:')

print('系统正在识别中...3')
time.sleep(1)
print('系统正在识别中...2')
time.sleep(1)
print('系统正在识别中...1')
time.sleep(1)

if [username,password] in database : print('Welcome! Access Granted')