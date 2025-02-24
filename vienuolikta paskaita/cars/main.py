from car import Car
from electric_car import ElectricCar
from plain_car import PlainCar

cars = []

def add_car(car):
    cars.append(car)

if __name__ == '__main__':
    mercedes = Car('Mercedes', 'W211', 2005)
    honda = Car('Honda', 'Civic', 2010)
    
    mercedes.display_info()
    honda.display_info()
    
    tesla = ElectricCar('Tesla', 'Model S', 2020, 10000)
    
    tesla.display_info()
    tesla.charge()
    
    mitsubishi = PlainCar('Mitsubishi', 2005)
    subaru = PlainCar('Subaru', 2016)
    
    add_car(mitsubishi.get_data())
    add_car(subaru.get_data())
    print(cars)
    