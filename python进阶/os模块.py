import os

# pwd：print working directory
# get cwd current working directory
path = os.getcwd()
print(path)
# 全称 operating system
# 获取操作系统的名字
# nt windows系列  其它是 posix
print(os.name)
# 系统路径分隔符  separate windows \ other /
print(os.sep)

# 获取文件的绝对路径
print(os.path.abspath('data/json模块.json'))
# 判断是否是目录 directory 绝对路径
print(os.path.isdir(os.path.join(path, './data/json模块.json')))
print(os.path.isdir(os.path.join(path, './data')))
# 相对路径
print(os.path.isdir('./data'))

# 判断是否是文件
print(os.path.isfile('./data/json模块.json'))

# 是否存在 文件或目录
print(os.path.exists('./data/tmp'))
print(os.path.exists('./data'))

# 文件名 文件后缀
# os.path.splitext()
'''
os.getcwd()  # 获取当前的工作目录，即当前python脚本工作的目录
os.chdir('test')  # 改变当前脚本工作目录，相当于shell下的cd命令
os.rename('毕业论文.txt', '毕业论文-最终版.txt')  # 文件重命名
os.remove('毕业论文.txt')  # 删除文件
os.rmdir('demo')  # 删除空文件夹
os.removedirs('demo')  # 删除空文件夹
os.mkdir('demo')  # 创建一个文件夹
os.chdir('C:\\')  # 切换工作目录
os.listdir('C:\\')  # 列出指定目录里的所有文件和文件夹
os.environ.get('PATH')  # 获取指定的环境配置
os.path.abspath(path)  # 获取Path规范会的绝对路径
os.path.exists(path)  # 如果Path存在，则返回True
os.path.isdir(path)  # 如果path是一个存在的目录，返回True。否则返回False
os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
os.path.splitext(path)  # 用来将指定路径进行分隔，可以获取到文件的后缀名
'''
