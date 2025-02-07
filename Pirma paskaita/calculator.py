import os

os.system('cls')


task = None

while True:
    digit1 = 0
    digit2 = 0

    usedDigit1 = float(input("Please enter the first number: "))
    os.system('cls')

    print('1) +')
    print("2) -")
    print("3) *")
    print("4) /")
    print("5) ^")
    print("6) %")

    choice = input("Please select: ")

    os.system('cls')

    if choice == "1":
        usedDigit2 = float(input("Select a number you want to add: "))
        result = usedDigit1 + usedDigit2
        print(f"Result: {result}")
        break
    elif choice == "2":
        usedDigit2 = float(input("Select a number you wnat to decrement: "))
        result = usedDigit1 - usedDigit2
        print(f"Results: {result}")
        break
    elif choice == "3":
        usedDigit2 = float(input("Select a number you want to multiply: "))
        result = usedDigit1 * usedDigit2
        print(f"Results: {result}")
        break
    elif choice == "4":
        usedDigit2 = float(input("Select a number you want to divide: "))
        result = usedDigit1 / usedDigit2
        print(f"Results: {result}")
        break
    elif choice == "5":
        usedDigit2 = float(
            input("Select number by which you want to multiply by the root: "))
        result = usedDigit1 ** usedDigit2
        print(f"Results: {result}")
        break
    elif choice == "6":
        usedDigit2 = float(
            input("Select number by which you want to modulus: "))
        result = usedDigit1 % usedDigit2
        print(f"Results: {result}")
        break
    else:
        print("Wrong selection")
