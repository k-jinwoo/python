"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 실습 중복 제거 예 교재 p98
"""

# 중복 원소를 갖는 리스트
gender = ['남','여','남','여']

# 중복 원소 제거
sgender = set(gender) # list -> set
lgender = list(sgender) # set -> list
print(lgender)

print(lgender[1])