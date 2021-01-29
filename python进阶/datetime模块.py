import datetime

# _xxx 私有
# __xx__魔方方法
# xx_ 关键词冲突
# datetime 类
import time

# https://blog.csdn.net/cmzsteven/article/details/64906245
a = datetime.datetime.now()
print(a)
print(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond)
print(a.weekday(), a.isoweekday())
# 返回datetime对象的日期部分
print(a.date())
# 返回datetime对象的时间部分
print(a.time())
# 返回UTC时间元组 表示方法如下： "yyyy-MM-dd 'T' HH:mm:ss.SSS Z"
print(a.utctimetuple())
# 返回当前日期时间的UTC datetime对象
print(datetime.datetime.utcnow())
# 根据string, format 2个参数，返回一个对应的datetime对象
# string to parse
print(datetime.datetime.strptime('2021-1-23 15:25', '%Y-%m-%d %H:%M'))
# UTC时间戳的datetime对象，时间戳值为time.time()
print(datetime.datetime.utcfromtimestamp(time.time()))

# date 类
b = datetime.date.today()
print(b)
print(b.year, b.month, b.day)
# 计算日期的差
c = datetime.date(2021, 1, 20)
print(b - c)

# iso 标准化
print(b.isocalendar())
print(b.isoformat())
print(b.weekday(), b.isoweekday())
# 格式化输出
print(b.strftime('%Y->>%m->>%d'))
# 猜测是这样
print(b.ctime())

# 时间间隔
d = datetime.timedelta(20)
print(b + d)
print(a.timestamp())
e = a.timestamp()
print(datetime.datetime.fromtimestamp(e), datetime.datetime.utcfromtimestamp(e))
