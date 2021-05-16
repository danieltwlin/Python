import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
#
# 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
# 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
# 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
# 4.之後提款 700 元, pytest 預期會接到 RuntimeError
#
##########################################################################################
    @classmethod
    def setup_class(cls):
        # init
        customer1 = Customer("Test User","100-1100")
        # deposit
        customer1.deposit(INIT_MONEY)
        cls.customer1 = customer1

    def test_deposit(self):
        self.customer1.deposit(1000)
        balance = self.customer1.balance
        assert  balance == 1100
        
    def test_withdraw(self):
       self.customer1.withdraw(500)
       balance = self.customer1.balance
       assert  balance == 600
       
    def test_interest(self):
       customer1 = self.customer1
       CustomerDataProcess1 = CustomerDataProcess()
       balance = CustomerDataProcess1.add_interest(customer1,0.1)
       balance2 = Decimal(balance).quantize(Decimal('.00'), ROUND_DOWN)
       assert  balance2 == 660
       
    def test_withdraw2(self):    
        with pytest.raises(Exception): 
            self.customer1.withdraw(700)
        