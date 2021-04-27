"""
날짜 : 2021/04/26
이름 : 김진우
내용 : 파이썬 String 예제 교재 p48
"""

# 문자열 더하기
str1 = 'Hello'
str2 = "Python"
str3 = str1 + str2
print('str3 :', str3)

# 문자열 곱하기
name = '홍길동'
print('name * 3 :', name *3)

# 문자열 길이
msg = 'Hello World'
print('msg 길이 :', len(msg))

# 문자열 인덱스
print('msg 1번째 문자 :', msg[0])
print('msg 7번째 문자 :', msg[6])
print('msg -1번째 문자 :', msg[-1]) # 뒤에서 부터
print('msg -5번째 문자 :', msg[-5])

# 문자열 자르기 (substring)
print('msg 0~5 까지 문자열 :', msg[0:5])
print('msg 처음~5 까지 문자열 :', msg[:5]) # 시작점이 없으면 처음번호로 지정
print('msg 6~11 까지 문자열 :', msg[6:11])
print('msg 6~마지막 까지 문자열 :', msg[6:]) # 종료점이 없으면 마지막번호로 지정

# 문자열 분리
people = '김유신^김춘추^장보고^강감찬^이순신' # 분리되는것 하나당 token
p1, p2, p3, p4, p5 = people.split('^') # 구분자 지정을 해줘야함

print('p1 :', p1)
print('p2 :', p2)
print('p3 :', p3)
print('p4 :', p4)
print('p5 :', p5)

# 문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주') # \n는 new line(다음줄)
print('서울\t대전\t대구\t부산\t광주') # \t는 tap (한칸씩 띄워주기)
print('저는 \'홍길동\' 입니다.') # \'는 '로 출력되게 함
print("저는 '홍길동' 입니다.")