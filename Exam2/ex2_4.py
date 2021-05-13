"""
날짜 : 2021/05/13
이름 : 김진우
내용 : 파이썬 Exam2_4 실습
"""

import  math, random

def lotto() :
    lotto_set = set()

    while True :
        num = math.ceil(random.random()*45)
        lotto_set.add(num)

        if len(lotto_set) == 6 :
            break

    return list(lotto_set)

if __name__ == '__main__' :
    for i in range(5) :
        lotto_nums = lotto()
        lotto_nums.sort()
        print(lotto_nums)