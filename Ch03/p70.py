"""
날짜 : 2021/04/28
이름 : 김진우
내용 : 실습 for 반복문 예 교재 p70
"""

# (1) 문자열 열거형객체 이용
string = "홍길동"
print(len(string)) # 문자 길이 : 3
for s in string : # 1문자 -> 변수 넘김 : 3회
    print(s)

# (2) list 열거형객체 이용
lstset = [1,2,3,4,5] # 5개 원소를 갖는 열거형객체
for e in lstset :
    print('원소 : ', e)