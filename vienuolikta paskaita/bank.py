class Bank:
    def __init__(self, balance):
        self.stocks = 0
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__helper_balance()
    
    def __helper_balance(self):
        return self.__balance + self.stocks
    
alan = Bank(10)
kirill = Bank(10000)

alan.deposit(100)
print(kirill.get_balance())
print(alan._Bank__helper_balance())
print(kirill.__balance)
print(alan.stocks)

