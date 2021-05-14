def asd(x) :
    if x < 10 :
        return '수수료는 없습니다.'
    elif x >= 10 :
        return '수수료는 10,000원 입니다.'
x = int(input('짐의 무게는 얼마입니까? : '))
print(asd(x))