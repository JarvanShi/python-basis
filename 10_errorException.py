import traceback

# 捕获异常
try:
    print('---------------')
    open('123.txt', 'r')
    print(num)
    print('---------------')
except (IOError, NameError) as errMsg:
    print(errMsg)
else:
    print('没有出错')
finally:
    print('这句话肯定会执行')