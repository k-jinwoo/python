"""
날짜 : 2021/04/28
이름 : 김진우
내용 : 실습 단일 조건문 형식2 예문 교재 p62
"""

# 100~85 : '우수', 84~70: '보통', 69이하 : '저조'
score = int(input('점수 입력 : '))
if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

# 중첩 조건문 예
score = int(input('점수 입력 : '))
grade = '' # 등급

if score >= 85 and score <= 100 :
    grade = '우수'
elif score >= 70 :
        grade = '보통'
else :
        grade = '저조'

print('당신의 점수는 %d이고, 등급은 %s'%(score,grade))