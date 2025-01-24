# Logikos operatoriai

testinis = int(input("Enter a number: "))

if testinis % 3 == 0 or testinis % 5 == 0:
    print('"if" ran!')
else:
    print('"else" ran!')

# \
print("Testing purposes \"this\"")


num = float(input("Enter a number: "))
if(num > 0):
    print("Number is positive")
else:
    print("Number is negative")


age = int(input("Enter your age: "))
if(age >= 18):
    print("User is full grown")
else:
    print("User is small")
    
    
# 1-2-3-4-5-6-(7)-8-9-10-11-12-13-(14)
result = 0
for x in range(101):
    if(x % 7 == 0):
        result = result+1

print(result)

