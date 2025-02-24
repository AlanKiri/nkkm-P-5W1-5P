from os import system
from time import sleep

def clear():
    system('cls')

class Budget():
    def __init__(self):
        self.budget = 0
        self.monthly_spendings = None
   
    def increase_budget(self):
        while True:
            clear()
            print("How much money do you want to deposit?: ")
            amount = int(input())
            if amount < 0:
                continue
            self.budget += amount
            break

    def decrease_budget(self):
        while True:
            clear()
            print('How much money do you want to withdraw: ')
            amount = int(input())
            if amount < 0:
                continue
            self.budget -= amount
            break

    def change_monthly(self):
        while True:
            clear()
            print(f"Your current monthly spendings is {self.monthly_spendings} {
                '' if self.monthly_spendings is None else '$'}")
            print('Input new value: ')
            new_monthly = int(input())
            if new_monthly < 0:
                continue
            self.monthly_spendings = new_monthly
            break
            
    def calculate_months(self):
        while True:
            clear()
            if self.monthly_spendings == 0 or self.monthly_spendings is None:
                break
            
            amount = int(input('How much months are we calculating?: '))
            if (amount < 0 or amount > 60):
                continue
            result = 0
            for _ in range(amount):
                result += self.monthly_spendings
            return result
        
if __name__ == '__main__':
    my_budget = Budget()
    while True:
        clear()
        print(f"Current balance {my_budget.budget}")
        print(f"Monthly spendings {my_budget.monthly_spendings}{
            '' if my_budget.monthly_spendings is None else '$'}")
        print("What do you want to do?")
        print("(1) Increase budget. (2) Decrease budget. (3) Reset budget. (4) Change montly spendings. (5) Calculate. (0) Exit.")

        try:
            choice = int(input())
            if choice in (1, 2, 3, 4, 5, 0):
                match(choice):
                    case 1:
                        my_budget.increase_budget()
                    case 2:
                        my_budget.decrease_budget()
                    case 3:
                        my_budget.budget = 0
                    case 4:
                        my_budget.change_monthly()
                    case 5:
                        print(my_budget.calculate_months())
                        sleep(5)
                    case 0:
                        exit()
        except ValueError:
            print('ValueError')
            sleep(2)
        except TypeError:
            print('TypeError')
            sleep(2)