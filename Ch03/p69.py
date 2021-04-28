"""
날짜 : 2021/04/28
이름 : 김진우
내용 : 실습 break, continue 예 교재 p69
"""

i = 0
while i < 10:
    i += 1 # 카운터
    if i == 3:
        continue # 다음 문장 skip
    if i == 6 :
        break # exit
    print(i, end=' ')