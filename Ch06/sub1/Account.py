# 클래스 정의
class Account: # 클래스는 대문자로 시작
    # 속성 (데이터)
    def __init__(self, bank, id, name, money): # __ = 특수 함수
        self.bank = bank       # Account 맴버의 변수
        self.id = id
        self.name = name
        self.money = money

    #기능
    def deposit(self, money):
        self.money += money
    def withdraw(self, money):
        self.money -= money
    def show(self):
        print('----------------------')
        print('은행명 :', self.bank)
        print('계좌번호 :', self.id)
        print('예금주 :', self.name)
        print('현재잔액 :', self.money)