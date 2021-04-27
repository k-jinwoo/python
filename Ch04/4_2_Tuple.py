"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 파이썬 자료구조 Tuple 실습 교재 p92
"""
# List - 여러 개의 자료를 순서대로 적재하는 가변 길이 순차 자료구조를 생성하는 클래스
# Tuple - List와 비슷하지만 읽기전용으로 원소를 수정,삭제가 불가능 List보다는 처리 속도가 빠름
# Set - 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스 (중복 X)
# Dictionary - 사전형으로 여러 개의 자료를 비 순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스
#               Set과 차이점은 key에 value을 저장하고, 키를 통해 값을 참조하는 형식

# Tuple (고정 List) 생성
tuple1 = (1,2,3,4,5) # List = [] / Tuple = ()
print('tuple type :', type(tuple1))
print('tuple1[0] :', tuple1[0])
print('tuple1[4] :', tuple1[4])

tuple2 = ('서울','대전','대구','부산','광주')
print('tuple2 type :', type(tuple2))
print('tuple2[0] : %s' % tuple2[0])
print('tuple2[4] : {}'.format(tuple2[4]))

# tuple 수정, 추가, 삭제 X
tuple3 = 1,2,3,4,5
print('tuple3 type :', type(tuple3))

# tuple3[1] = 7 - 수정 에러
# tuple3[4] = [] - 삭제 에러