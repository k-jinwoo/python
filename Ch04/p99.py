"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 실습 딕트 객체 예 교재 p99
"""

# (1) dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성 방법2
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# (3) 원소 수정, 삭제, 추가
# dict 원소 수정
person['age'] = 45
print(person)

# dict 원소 삭제
del person['address']
print(person) # {'name' : '홍길동', 'age' : 45}

# dict 원소 추가
person['pay'] = 350
print(person) # {'name' : '홍길동', 'age' : 45, 'pay' : 350}