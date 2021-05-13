"""
날짜 : 2021/05/13
이름 : 김진우
내용 : 코딩 테스트 - 큰 수의 법칙
"""

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
result = 0
a = 0
b = 0
for i in range(n-1) :
    data.sort()
# result = 0
# repeat = k
# data.sort(reverse=True) 리스트를 내림차순으로 정렬
# first = data[0]
# second = data[1]
for j in range(m) :
    if a != k :
        result += data[n-1]
        a += 1
    # if repeat > 0 :
        # result += first
        # repeat -= 1
    elif a == k :
        m-= 1
        result += data[n-2]
        a = 0
        b += 1
    #else :
        # result += second
        # repeat = k
# m = m + b

print('n : %d, m : %d, k : %d' % (n, m, k))
print('data :', data)

# 최종 답안 출력
print(result)