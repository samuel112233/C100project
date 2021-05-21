class Atm(object):
    def __init__(self,atmCard,pinNumber):
        self.atmCard=atmCard
        self.pinNumber=pinNumber
    
    def cashWithdrawl(self):
        print('Cash Withdrawed')

    def cashDeposition(self):
        print('Cash Deposited')

    def balanceEnquiry(self):
        print('Balance Enquired')
    
    def amountOfCashWithdrawl(self,amount):
        print('Amount of cash withdrawed ',amount)

    def amountOfCashDeposition(self,amount):
        print('Amount of cash deposited ',amount)

SBI=Atm('SBI Atm card','1234')
print(SBI.pinNumber)
SBI.cashWithdrawl()
SBI.cashDeposition()
SBI.balanceEnquiry()
SBI.amountOfCashWithdrawl(500)
SBI.amountOfCashDeposition(3000)
    
