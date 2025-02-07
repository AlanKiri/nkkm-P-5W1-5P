import os
import random
import time

products = {
    "eggs": 20,
    "oranges": 30,
    "beetroot": 15,
    "fish": 22,
    "onions": 0,
    "garlic": 0,
    "flour": 15,
    "olive_oil": 4,
}

prices = {
    "eggs": 3,
    "oranges": 2,
    "beetroot": 3,
    "fish": 5,
    "onions": 1,
    "garlic": 1,
    "flour": 2,
    "olive_oil": 4,
}

while True:
    start = input(f"Hello, currently we have {len(
        products)} products in stock. If you want to proceed with stock check press enter: ")
    break

os.system('cls')

for i in products:
    product = products[i]
    price = prices[i]
    if (product < 10):
        bought = random.randint(10, 25)
        products[i] += bought
        print(f"Ordered {bought} positions for {i} price is {bought * price}")

print('Displaying new information in 2 seconds...')
time.sleep(10)

os.system('cls')
print("Results: ")
for i in products:
    print(f"{i} : {products[i]}")

print("Waiting for 2 seconds before closing the app")
time.sleep(2)
