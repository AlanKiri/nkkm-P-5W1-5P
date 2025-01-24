x = 10
y = 3.14
z = "hello"
print(type(x), type(y), type(z))


a = 5
b = 10
# a = 10, b = 5

# Bad
# c = a
# a = b 
# b = c

a, b = b, a
print(a, b)


name =  input("Please write you name: ")
age = input("Please write your age: ")
# Nepamirškit f prieš ""
result = f"Hello, my name is {name} and i'm {age} years old"
print(result)


num = 3.99
converted_num = int(num)
print(num, converted_num)
print(type(converted_num))
# 3.99, 3


# labas -> sabal
string = input("Enter something: ")

reversedString1 = ""
for x in reversed(string):
    reversedString1+=x
print(reversedString1)

reversed_string2 = string[::-1]
print(reversed_string2)


sentence = input("Please write in an sentence: ")
words = sentence.split()
print(len(words), type(words))


replaceTask = input("Please write text in which you want to replace: ")
# Konvertuojam visas raides i mazas
replaceTask = replaceTask.lower()
replaceTask = replaceTask.replace('hello', 'good bye')
print(replaceTask)


extractedBefore = "I think this class is clean today"
extractedBefore = extractedBefore[3:6]
print(extractedBefore)


radius = float(input("Enter a float value: "))
area = 3.14159 * radius ** 2
print(f"Result is: {area}")


p = float(input('Input principal: '))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print(f"Simple interest: {si}")


# Loops 

for i in range(11):
    print(i)

i = 1
while i<= 10:
    i+=1
    
for i in range(2, 51):
    print(i)
    
    


    
    