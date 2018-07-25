import time

# 格式化时间
datetime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(datetime)
# 去格式化时间
date = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
print("-----", date)
# 转换成时间戳
datemk = time.mktime(date)
print(datemk, time.time())
date = time.localtime()
print(time.mktime(date))
