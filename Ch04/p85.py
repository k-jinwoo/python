"""
날짜 : 2021/04/29
이름 : 김진우
내용 : 실습 단일 리스트 객체 예 교재 p85
"""

# (1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst :
    print(lst[:i]) # i 전까지