import os 
import sys
import time

def clear():
    os.system('cls')
    
def print_result(bmi):
    clear()
    print(f"Your BMI is {result}")
    if(result >= 40):
        print('Obese')
    elif(result >= 25):
        print("Overweight")
    elif(result >= 18.5):
        print('Normal')
    else:
        print('Underweight')
        
    time.sleep(5)
    
while True:
    clear()
    print('Welcome to BMI calculator! Please type your units to start. (metric, us, exit)')
    
    units = input()
    
    if units in ('metric', 'us', 'exit'):
        match(units.lower()):
            case "exit":
                sys.exit()
            case "_":
                continue
    else:
        continue
    
    weight = None
    while weight is None:
        clear()
        
        try:
            print(f"Please enter your weight in {'kg' if units == 'metric' else 'lbs'}.")
            weight = int(input())
        except ValueError:
            print('You inputted a wrong number.')
            time.sleep(3)
            continue
    
    height = None
    while height is None:
        clear()
        
        try:
            print(f"Please enter your height in {'cm' if units == 'metric' else 'ft'}.")
            height = float(input())
        except ValueError:
            continue
    
    if(units == 'metric'):
        height = height / 100
        
    result = None
    if units == 'metric':
        result = weight / height**2
    elif units == 'us':
        result = weight / (height*12) ** 2 * 703
    result = round(result, 1)
    
    print_result(result)
    
    
        
    
    
        