class MyNumber:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return f"My result is {self.value}"
    
    def number_plus(self):
        self.value+=1
        
    def number_minus(self):
        self.value-=1
    
number_1 = MyNumber(5)
number_2 = MyNumber(10)

for x in range(10):
    number_1.number_plus()
    number_2.number_plus()
        
for x in range(5):
    number_1.number_minus()
    
print(number_1)
print(number_2)
    