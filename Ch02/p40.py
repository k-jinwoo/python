"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 실습 관계연산자 예 교재 p40
"""

num1 = 2
num2 = 1
# (1) 동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)

# (2) 크기비교
bool_result = num1 > num2 # num1값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2 # num2값이 크거나 같은지 비교
print(bool_result)

"""
내용 : 실습 논리 연산자 예 교재 p40
"""

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <=10
print(log_result)

# 두 관게식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <=10
print(log_result)

log_result = num1 >= 50 #관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)