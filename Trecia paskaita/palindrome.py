task = input("Please input something atleast: ").strip()

if task == task[::-1]:
    print('palindrome')
else:
    print('not palindrome')
