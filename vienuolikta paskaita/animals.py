class Animal():
    def __init__(self, age):
        self.age = age
    
    def get_age(self):
        print(self.age)
        
class Dog(Animal):
    def __init__(self, age, color):
        super().__init__(age)
        self.color = color
    
    def get_color(self):
        print(self.color)
        
    def get_age(self):
        print(f"This is my new 'get_age' function.")
        
white = Dog(5, 'white')
black = Dog(10, 'black')
violet = Dog(15, 'violet')

white.get_age()
black.get_color()
print(violet.age)

