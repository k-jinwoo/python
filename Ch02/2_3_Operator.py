"""
날짜 : 2021/04/26
이름 : 김진우
내용 : 파이썬 연산자 실습하기 교제 p38
"""

# 대입연산자 - 파이썬에서는 True False 는 첫글자가 대문자
a = 1
b = c = d = 0
e, f, g = 7, True, 'Apple'

print('a :', a)
print('c :', c)
print('f :', f)
print('g :', g)

# 산술연산자
num1 = 1
num2 = 2
num3, num4 = 3, 4

r1 = num1 + num2
r2 = num1 - num2
r3 = num2 * num3
r4 = num4 / num2
r5 = num4 % num3
r6 = num4 ** num2
r7 = num4 // num2

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)
print('r5 :', r5)
print('r6 :', r6)
print('r7 :', r7)

# 복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8

num5 += 1
num6 -= 2
num7 *= 3
num8 /= 4

print('num5 :', num5)
print('num6 :', num6)
print('num7 :', num7)
print('num8 :', num8)

# 비교연산자
var1 = 1
var2 = 2

rs1 = var1 > var2
rs2 = var1 < var2
rs3 = var1 >= var2
rs4 = var1 <= var2
rs5 = var1 == var2
rs6 = var1 != var2

print('rs1 :', rs1)
print('rs2 :', rs2)
print('rs3 :', rs3)
print('rs4 :', rs4)
print('rs5 :', rs5)
print('rs6 :', rs6)

# 논리연산자
var3 = 3
var4 = 4

res1 = (var3 > 2) and (var4 > 3) # var 3은 2보다 크고 그리고 var4는 3보다 크다
res2 = (var3 > 2) and (var4 > 4) # var 3은 2보다 크고 그리고 var4는 4보다 크다
res3 = (var3 > 2) or (var4 > 4)  # var 3은 2보다 크고 또는 var4는 4보다 크다
res4 = not (var3 > var4) # var 3은 var4 보다 크지 않다

print('rse1 :', res1)
print('rse2 :', res2)
print('rse3 :', res3)
print('rse4 :', res4)