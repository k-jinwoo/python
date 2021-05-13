"""
날짜 : 2021/05/13
이름 : 김진우
내용 : 코딩 테스트 - 숫자 카드 게임
"""


n, m = map(int, input().split())
nums = []
result = 0

for i in range(n) :
    data = list(map(int, input().split()))

    # data에서 가장 작은 값 구하기
    data.sort()
    num = data[0]
    nums.append(num)

# nums에서 가장 큰 값 구하기
nums.sort()
result = nums[-1]

print(result)