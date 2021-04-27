"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 실습 대입연산자 예 교재 p41
"""

# (1) 변수에 값 할당 (=)
i = tot = 10 # i=10; tot=10
i += 1 # i = i + 1
tot += i # tot = tot + i
print(i,tot)

# 같은 줄에 중복 출력
print('출력1', end=' , ') # end='구분자'
print('출력2')

v1, v2 = 100, 200

# 변수 교체
v2, v1 = v1, v2
print(v1,v2) # 200 100

# (3) 패킹(packing) 할당
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1,v2) # 1 [2,3,4,5]

*v1, v2 = lst
print(v1,v2) # [1,2,3,4]5