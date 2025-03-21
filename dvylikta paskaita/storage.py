from random import randint

class Storage:
    coffee_recipes = {
        "espresso": {
            "coffee_ground": 7,  # grams
            "water": 30  # ml
        },
        "americano": {
            "coffee_ground": 7,  # grams
            "water": 150  # ml
        },
        "cappuccino": {
            "coffee_ground": 7,  # grams
            "milk": 60,  # ml
            "milk_steamed": True,
            "milk_foam": 60,  # ml
            "foam_steamed": True
        },
        "latte": {
            "coffee_ground": 7,  # grams
            "milk": 150,  # ml
            "milk_steamed": True,
            "milk_foam": 10,  # ml
            "foam_steamed": False
        },
        "flat white": {
            "coffee_ground": 7,  # grams
            "milk": 150,  # ml
            "milk_steamed": True
        },
        "macchiato": {
            "coffee_ground": 7,  # grams
            "milk_foam": 15,  # ml
            "foam_steamed": False
        },
        "mocha": {
            "coffee_ground": 7,  # grams
            "milk": 150,  # ml
            "chocolate_syrup": 15,  # grams
            "milk_steamed": True,
            "milk_foam": 50,  # ml
            "foam_steamed": True
        },
        "cortado": {
            "coffee_ground": 7,  # grams
            "milk": 40,  # ml
            "milk_steamed": True
        },
        "affogato": {
            "coffee_ground": 7,  # grams
            "vanilla_ice_cream": 60  # grams
        },
        "latte macchiato": {
            "coffee_ground": 7,  # grams
            "milk": 200,  # ml
            "milk_steamed": True,
        },
        "ristretto": {
            "coffee_ground": 7,  # grams
            "water": 20  # ml
        },
        "turkish coffee": {
            "coffee_ground": 10,  # grams
            "water": 50,  # ml
            "sugar": 10  # grams
        }
    }
    
    def __init__(self):
        self.ingredients = {
            "water":0,
            "milk": randint(1000, 2000),
            "milk_foam": randint(100, 500),
            "coffee_beans": randint(500, 1000),
            "coffee_ground": 0,
            "chocolate_syrup": 200,
            "vanilla_ice_cream": 250,
            "sugar": 100
            }
        
    def check_drink_stock(self, drink:str):
        result = True
        for ingredient, required_stock in self.coffee_recipes[drink].items():
            if ingredient in self.ingredients and not self.check_ingredient_stock(ingredient, required_stock):
                result = False
        return result
        
    def check_ingredient_stock(self, ingredient:str, required_stock:int):
        if ingredient in self.ingredients:
            if ingredient == 'coffee_ground' and (self.ingredients[ingredient] > required_stock or self.ingredients['coffee_beans'] > required_stock):
                return True
            elif self.ingredients[ingredient] > required_stock:
                return True
            else:
                return False
        else:
            return None        
        
    def remove_used_ingredients(self, ingredients):
        for ingredient, required_stock in ingredients.items():
            if ingredient in self.ingredients:
                self.ingredients[ingredient] -= required_stock
        
    def grind_coffee_beans(self, amount):
        self.ingredients['coffee_ground']+=amount
        self.ingredients['coffee_beans']-=amount
        
    def order_ingredients(self, ingredient):
        arrived_stock = randint(100,300)
        self.ingredients[ingredient] += arrived_stock
        return arrived_stock