"""
날짜 : 2021/05/13
이름 : 김진우
내용 : 파이썬 Exam2_2 실습
"""

def gcd(a, b) :
    temp = 0

    if a<b :
        temp = a
    else :
        temp = b

    while True :
        if a % temp == 0 and b % temp == 0 :
            break
        temp -= 1

    return  temp
if __name__ == '__main__' :
    print('1과 5의 최대공약수 :', gcd(1,5))
    print('2과 5의 최대공약수 :', gcd(2,6))
    print('3과 9의 최대공약수 :', gcd(3,9))
    print('18과 12의 최대공약수 :', gcd(18,12))
    print('60과 24의 최대공약수 :', gcd(60,24))