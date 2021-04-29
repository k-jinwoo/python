"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 실습 단일 리스트 색인 예 교재 p86
"""

# (2) 단일 list 색인
x = list(range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2]) # 홀수 색인
print(x[1::2]) # 1부터 시작 하는 짝수 색인 (start:stop:step)