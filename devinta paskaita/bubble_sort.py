from random import sample

numbers = sample(range(1, 10001), 100)

print(f"Initial array: {numbers}")

for x in range(len(numbers)):
    for y in range(len(numbers)):
        if y == len(numbers)-1:
            continue
        if numbers[y] > numbers[y+1]:
            numbers[y], numbers[y+1] = numbers[y+1], numbers[y]
        

print(f"Result array: {numbers}")