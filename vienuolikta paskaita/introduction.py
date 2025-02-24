number = 0
number_two = 5

def plus_number (number):
    number+=1
    return number
    
def minus_number(number):
    number-=1
    return number

number = plus_number(number)

for x in range(10):
    number = plus_number(number)
    number_two = plus_number(number_two)
    
for x in range(5):
    number = minus_number(number)

print(number)
print(number_two)
    
