"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 파이썬 리스트 함수 교재 p88
"""

dataset = [1,4,3]
print('1.dataset :', dataset)

# list 원소 추가
dataset.append(2)
dataset.append(5)
print('2.dataset :', dataset)

# list 정렬
dataset.sort()
print('3.dataset :', dataset) # 오름차순

dataset.sort(reverse=True)
print('4.dataset :', dataset) # 내림차순

# list 원소 삽입
dataset.insert(2,6)
dataset.insert(1,7)
print('5.dataset :', dataset) # (index,value) 2번자리에 6을 넣어라

# list 원소 삭제
dataset.remove(6)
print('6.dataset :', dataset) # 6을 삭제

# map 함수
# - 리스트 원소를 지정된 함수로 일괄 처리해주는 함수
# - 여러 개의 데이터를 한번에 다른 형태로 변환할 때 많이 사용
def plus10(n):
    return  n+10

list1 = [1,2,3,4,5]
list1_map = map(plus10,list1)
print('list1_map :', list1_map)
list1_map_list = list(list1_map) # list1_map_list = list(map(plus10,list1)
print('list1_map_list :', list1_map_list)

list2 = [1.1,2.2,3.3,4.4,5.5]
#var1 = 1.1
#result = int(var1)              result = 1 (실수자리 제외 / 반올림 X)
#print('result :', result)
list2_map_list = list(map(int,list2)) # 정수로 모두 변환 1.1 -> 1
print('list2_map_list :', list2_map_list)

list3 = [1,2,3,4,5]
list3_map_list = list(map(lambda x:x*2,list3))
print('list3_map_list :', list3_map_list)

list4 = ['1','2','3','4','5']
list4_map_list = list(map(int,list4)) # str -> int
print('list4_map_list :', list4_map_list)
print('list4_map_list[0] type :', type(list4_map_list[0])) # int를 사용해 str(문자열)에서 정수로 변환된 모습

# input 함수 확장 - 파이썬 기본 입력 함수
a = input('입력 : ')
print('a :', a)

var1 , var2, var3 = input('3개 숫자 입력(띄어쓰기 구분) : ').split() # str로 값을 받음
print('var1 : {}, var2 : {}, var3 : {}'.format(var1,var2,var3))
print('var1 + var2 + var3 = ', var1+var2+var3)

num1 , num2, num3 = map(int,input('3개 숫자 입력(띄어쓰기 구분) : ').split()) # int로 값을 받음
print('num1 : {}, num2 : {}, num3 : {}'.format(num1,num2,num3))
print('num1 + num2 + num3 = ', num1+num2+num3)