from random import sample

numbers = sample(range(1, 10001), 5)

print(f"Initial array: {numbers}")

for x in range(len(numbers)):
    smallest_index = x
    
    for y in range(x, len(numbers)):
        if numbers[y] < numbers[smallest_index]:
            smallest_index = y
    
    if smallest_index != x:
        numbers[x], numbers[smallest_index] = numbers[smallest_index], numbers[x]

print(f"Result array: {numbers}")