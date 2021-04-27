"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 파이썬 자료구조 리스트 실습 교재 p84
"""
# List - 여러 개의 자료를 순서대로 적재하는 가변 길이 순차 자료구조를 생성하는 클래스
# Tuple - List와 비슷하지만 읽기전용으로 원소를 수정,삭제가 불가능 List보다는 처리 속도가 빠름
# Set - 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스 (중복 X)
# Dictionary - 사전형으로 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스
#               Set과 차이점은 key에 value을 저장하고, 키를 통해 값을 참조하는 형식

# 리스트 생성
list1 = [1,2,3,4,5] # 일반 리스트

print('list1 type :', type(list1))
print('list1[0] :', list1[0])
print('list1[2] :', list1[2])
print('list1[3] :', list1[3])

list2 = [5, 3.14, True, 'Apple'] # 다른 형태의 내용물

print('list2 type :', type(list2))
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])
print('list2[3] :', list2[3])

list3 = [[1,2,3],[4,5,6],[7,8,9]] # 리스트 안에 리스트가 있는 경우

print('list3 type :', type(list3))
print('list3[0][0] :', list3[0][0])
print('list3[1][1] :', list3[1][1])
print('list3[2][1] :', list3[2][1])

# List 덧셈
animal1 = ['사자','호랑이','코끼리']
animal2 = ['곰','기린']

result = animal1 + animal2
print('result :', result)

# List 수정, 추가, 삭제
nums = [1,2,3,4,5]
print('nums :', nums)

nums[1] = 7 # 수정
print('nums :', nums)

nums[2:4] = [8,9,10] # 추가 2에서 4번자리 전까지
print('nums :', nums)

nums[3:5] = [] # 삭제 3에서 5번자리 전까지
print('nums :', nums)