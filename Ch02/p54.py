"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 실습 이스케이프 문자 기능 차단 예 교재 p54
"""

# (1) escape 문자 적용
print('escape 문자 차단 ')
print('\n출력 이스케이프 문자') # \n : 줄 바꿈 기능

# (2) escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')

# (3) 경로 표현 : C:\Python\test
print('path =', 'C:\Python\test')
print('path =', 'C:\\Python\\test')
print('path =', r'C:\Python\test')