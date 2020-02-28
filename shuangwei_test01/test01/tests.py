from base64 import encode

from django.test import TestCase

# Create your tests here.
import time

now = int(time.time())     # 1533952277
timeArray = time.localtime(now)
time_now = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(time_now)


print(encode('\u8be5\u7528\u6237\u5df2\u7ecf\u5b58\u5728 !!!'))