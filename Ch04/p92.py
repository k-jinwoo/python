"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 실습 리스트 내포 예 교재 p92
"""

# 형식1) 변수 = [ 실행문 for   ]
x = [2,4,1,5,7]
# print(x ** 2) # error

lst = [i ** 2 for i in x] # x변량에 제곱 계산
print(lst) # [4, 16, 1, 25, 49]

# 형식2) 변수 = [ 실행문 for if ]
# 1~10 -> 2의 배수 추출 -> i*2 -> list 저장
num = list(range(1,11))

lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)