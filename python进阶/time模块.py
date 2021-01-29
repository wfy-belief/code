import time

t = (2021, 1, 23, 19, 55, 59, 5, 23, 0)
print(time.asctime(t))
# return the current time in seconds since the Epoch.
print(time.time())
# Return the CPU time or real time since the start of the process or since
# the first call to clock().
print(time.process_time())
# gmtime
print(time.gmtime())
# local time
print(time.localtime())
# ctime
a = time.time()
print(time.ctime(a))
# mk time
b = time.localtime()
print(time.mktime(b))
