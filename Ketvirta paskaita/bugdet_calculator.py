from os import system
from sys import exit
from time import sleep

budget = 0
monthly_spendings = None


def clear():
    system('cls')


def increase_budget(budget):
    while True:
        clear()
        print("How much money do you want to deposit?: ")
        amount = int(input())
        if amount < 0:
            raise ValueError
        budget += amount
        return budget


def decrease_budget(budget):
    while True:
        clear()
        print('How much money do you want to withdraw: ')
        amount = int(input())
        if amount < 0:
            raise ValueError
        budget -= amount
        return budget


def change_monthly(monthly_spendings):
    clear()
    print(f"Your current monthly spendings is {monthly_spendings} {
          '' if monthly_spendings is None else '$'}")
    print('Input new value: ')
    new_monthly = int(input())
    if new_monthly < 0:
        raise ValueError
    return new_monthly


def calculate_months(monthly_spendings):
    if monthly_spendings == 0 or monthly_spendings is None:
        raise ValueError
    clear()
    amount = int(input('How much months are we calculating?: '))
    if (amount < 0 or amount > 60):
        raise ValueError
    result = 0
    for _ in range(amount):
        result += monthly_spendings
    return result


while True:
    clear()
    print(f"Current balance {budget}")
    print(f"Monthly spendings {monthly_spendings}{
          '' if monthly_spendings is None else '$'}")
    print("What do you want to do?")
    print("(1) Increase budget. (2) Decrease budget. (3) Reset budget. (4) Change montly spendings. (5) Calculate. (0) Exit.")

    try:
        choice = int(input())
        if choice in (1, 2, 3, 4, 5, 0):
            match(choice):
                case 1:
                    budget = increase_budget(budget)
                case 2:
                    budget = decrease_budget(budget)
                case 3:
                    budget = 0
                case 4:
                    monthly_spendings = change_monthly(monthly_spendings)
                case 5:
                    print(calculate_months(monthly_spendings))
                    sleep(5)
                case 0:
                    exit()
    except ValueError:
        print('ValueError')
        sleep(2)
    except TypeError:
        print('TypeError')
        sleep(2)
