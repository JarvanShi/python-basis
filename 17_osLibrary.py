import os.path

# 文件路径操作
abspath = os.path.abspath('hamlet.txt')
normpath = os.path.normpath(abspath.replace('/','\\'))
relpath = os.path.relpath('hamlet.txt')
dirname = os.path.dirname(abspath)
basename = os.path.basename(abspath)
name = os.path.join(dirname, basename)
exists = os.path.exists(abspath)
isfile = os.path.isfile(abspath)
isdir = os.path.isdir(abspath)

print('绝对路径：' + abspath)
print('======分割线======')
print('统一格式路径：' + normpath)
print('======分割线======')
print('相对路径：' + relpath)
print('======分割线======')
print('目录名：' + dirname)
print('======分割线======')
print('文件名：' + basename)
print('======分割线======')
print('路径名：' + name)
print('======分割线======')
print('路径是否存在：' + exists)
print('======分割线======')
print('是否是文件：' + isfile)
print('======分割线======')
print('是否是目录：' + isdir)

# 获取目录或文件上一次访问目录、上一次修改目录、创建目录、文件大小
print(os.path.getatime(abspath))
print(os.path.getmtime(abspath))
print(os.path.getctime(abspath))
print(os.path.getsize(abspath))

# 进程管理
os.system('C:/Windows/System32/mspaint.exe '.join(os.path.abspath('NewEra.jpg')))

# 环境参数
os.chdir()
os.getcwd()
os.getlogin()
os.cpu_count()
os.urandom(10)