"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 실습 요소 검사와 반복 예 교재 p100
"""

# (1) dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성 방법2
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# (1) 요소 검사
print(person['age']) # 45
print('age' in person) # True

# (2) 요소 반복
for key in person.keys() : # key 넘김
    print(key) # key 출력
for v in person.values() : # value 넘김
    print(v) # value 출력
for i in person.items() : # (key,value) 넘김
    print(i) # ('name', '홍길동')