"""
날짜 : 2021/05/13
이름 : 김진우
내용 : 파이썬 Exam2_1 실습
"""

scores = []

while True :
    print('0:종료, 1:입력')
    result = input('입력 : ')

    if result != '1' :
        break

    score = int(input('점수 입력 : '))
    scores.append(score)

print('입력한 점수 확인')
print(scores)

sum = 0

for score in scores :
    sum += score

print('리스트 총합 :', sum)