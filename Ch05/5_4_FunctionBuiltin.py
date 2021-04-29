"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 파이썬 내장함수 교재 p118
"""

import math
import random
import time

r1 = abs(-5)
print('r1 :', r1) # r1 : 5

# 올림
r2 = math.ceil(1.2)
r3 = math.ceil(1.8)
print('r2 :', r2) # r2 : 2 올림
print('r3 :', r3) # r3 : 2 올림

# 내림
r4 = math.floor(1.2)
r5 = math.floor(1.8)
print('r4 :', r4) # r4 : 1 내림
print('r5 :', r5) # r5 : 1 내림

# 반올림
r6 = round(1.2)
r7 = round(1.8)
print('r6 :', r6) # r6 : 1 반올림
print('r7 :', r7) # r7 : 2 반올림

# 제곱근
r8 = math.sqrt(4)
r9 = math.sqrt(9)
print('r8 :', r8) # r8 : 2.0 제곱근
print('r9 :', r9) # r9 : 3.0 제곱근

# random
num1 = random.random()
print('num1 :', num1) # num1 : 0.135989315 랜덤(0~1사이의 실수)

num2 = num1 * 10
print('num2 :', num2) # num2 : 0~10.452462463 랜덤(0~10사이의 실수)

num3 = math.ceil(num2)
print('num3 ;', num3) # num3 : 1~10 (1~10 사이의 정수)

num4 = math.ceil(random.random() * 10)
print('num4 :', num4) # num4 : 1~10 (1~10 사이의 정수)

# 날짜,시간
t1 = time.time() # Unix time
print('t1 :', t1)

t2 = time.ctime() # 변환된 Unix time
print('t2 :', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일' %(year,month,date))
print('%s시 %s분 %s초' %(hour,min,sec))