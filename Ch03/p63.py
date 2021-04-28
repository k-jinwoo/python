"""
날짜 : 2021/04/28
이름 : 김진우
내용 : 실습 삼항 조건문 예 교재 p63
"""

# (1) 일반 조건문
num = 9 # 초기화
result = 0

if num >= 5 :
    result = num * 2
else :
    result = num + 2
print('result =', result)

# (2) 3항 연산자
# 형식) 변수 = 참 if (조건문) else 거짓
result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2) # 18