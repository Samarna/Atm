class Atm():
    def __init__(self, atmCardNumber, pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self):
        print("Waiting for Withdrawl!")
    
    def BalanceEnquiry(self):
        print("Calculating Balance!")

card1 = Atm("1786 5764 8937 4658","1563")
card2 = Atm("8756 3475 1894 3333","1954")

print(card1.pinNumber)
print(card1.BalanceEnquiry())
print(card2.CashWithdrawl())