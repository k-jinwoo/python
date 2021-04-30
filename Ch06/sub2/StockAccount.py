# 출처
from Ch06.sub1.Account import Account

# 클래스 정의
class StockAccount(Account) : # (Account) = 상속 받음

    def __init__(self, bank, id, name, money, stock, amount, price):
        # self.bank = bank      - 상속받아서 필요없음
        # self.id = id
        # self.name = name
        # self.money = money

        # 부모클래스 생성자 실행
        super().__init__(bank,id,name,money)
        self.stock = stock
        self.amount = amount
        self.price = price

    # def deposit(self, money):
    #     self.money += money

    # def withraw(self, money):
    #     self.money -= money

    def sell(self, amount, price):
        print('{}를 {}개 {}가격에 판매함'.format(self. stock, amount, price))

    def buy(self, amount, price):
        print('{}를 {}개 {}가격에 구매함'.format(self.stock, amount, price))

    def show(self):
        super().show()
        print('주식종목 :', self.stock)
        print('주식수량 :', self.amount)
        print('주식가격 :', self.price)