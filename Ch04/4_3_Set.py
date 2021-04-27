"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 파이썬 자료구조 Set 실습 교재 p96
"""

# List - 여러 개의 자료를 순서대로 적재하는 가변 길이 순차 자료구조를 생성하는 클래스
# Tuple - List와 비슷하지만 읽기전용으로 원소를 수정,삭제가 불가능 List보다는 처리 속도가 빠름
# Set - 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스 (중복 X)
# Dictionary - 사전형으로 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스
#               Set과 차이점은 key에 value을 저장하고, 키를 통해 값을 참조하는 형식

# Set 생성
set1 = {1,2,3,4,5,3}
print('set1 type :', type(set1))
print('set1 :', set1) # 3은 중복이라서 12345만 출력

set2 = set('Hello World')
print('set2 type :', type(set2))
print('set2 :', set2) # 중복되는 문자 제외 공백 포함 8개 순서없이 출력

# 집합 출력 (List 변환)
list1 = list(set1)

print('list1 type :', type(list1))
print('list1 :', list1)
print('list1[0] :', list1[0])
print('list1[3] :', list1[3])

list2 = list(set2)
print('list2 :', list2)
print('list2[0] :', list2[0])
print('list2[3] :', list2[3])