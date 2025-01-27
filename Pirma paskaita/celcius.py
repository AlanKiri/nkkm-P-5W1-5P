import os

choice = None

print("Hello, please select: ")
print("1) Celsius to fahrenheit")
print("2) Fahrenheit to celsius")

choice = int(input())

os.system('cls')

if choice == 1:
  celsius = float(input("Please input celsius you want to convert: "))
  fahrenheit = 32 + (celsius*9/5)
  print(f"Result: {fahrenheit}fah.") 
if choice == 2:
  fahrenheit = float(input("Please input fahrenheit you want to convert: "))
  celsius = (fahrenheit - 32) * 5/9
  print(f"Result: {celsius}cel")
else:
  print("Wrong selection, sorry")
