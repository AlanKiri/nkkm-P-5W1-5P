from car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
        
    def charge(self):
        print(f"This car's battery size is {self.battery_size}")
        
  
if __name__ == '__main__':
    print('This class requires brand, model, year, battery size')