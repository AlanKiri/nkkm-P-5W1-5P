inputString = input("Please input a string: ")
for char in inputString:
    print(char)
    
while True:
    user_input = input("Please input your command: ").lower()
    if(user_input == 'hello'):
        print("Hello to you, stranger")
    elif(user_input == 'exit'):
        print("boo, you left")
        break
    

exampleString = 'Hello my name is string'
# 23

symbolCount = 0
for char in exampleString:
    symbolCount+=1
fastSymbolCount = len(exampleString)
print(symbolCount, fastSymbolCount)