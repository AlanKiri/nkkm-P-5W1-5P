class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
  
  
if __name__ == '__main__':
    print('This class requires brand, model, year')
