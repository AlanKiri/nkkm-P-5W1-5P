class PlainCar():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def get_data(self):
        return f"{self.brand} {self.year}"
        