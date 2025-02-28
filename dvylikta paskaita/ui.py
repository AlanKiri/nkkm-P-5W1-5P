from storage import Storage
import os 

class UI(Storage):
    main_menu_choices = ('1', '2', 'e', 'exit')
    
    
    def __init__(self):
        super().__init__()
        
    def clear(self):
        os.system('cls')
        
    def underscore(self, text):
        return f"\033[4m{text}\033[0m"
    
    def get_formatted_ingredient(self, ingredient, drink, formatted_ingredient=None):
        if formatted_ingredient is None:
            formatted_ingredient = ingredient
            
        required_stock = drink[ingredient]
        return formatted_ingredient if  self.check_ingredient_stock(ingredient, required_stock) else self.underscore(formatted_ingredient)
        
    def display_stock(self):
        for ingredient, stock in self.ingredients.items():
            print(f"{ingredient}: {stock} ml/g")
        print()
        
    def display_main_menu_selection(self):
        print("Welcome to the coffee machine! What's your plan?")
        print(f"1) Make a drink. 2) Restock the coffee machine. (e)xit")
        while True:
            choice = input()
            if choice not in self.main_menu_choices:
                continue
            else:
                return choice
            
    def coffee_machine_header(self):
        print("Coffee Machine")
            
    def drink_menu_selection(self):
        for key, drink in self.coffee_recipes.items():
            ingredients = ''
                
            ingredients += f"{drink['coffee_ground']} grams of {self.get_formatted_ingredient('coffee_ground', drink, 'ground')} "
            
            if 'water' in drink:
                    ingredients += f"{drink['water']} ml of {self.get_formatted_ingredient('water',  drink)}. "
            if 'milk' in drink:
                    ingredients += f"{drink['milk']} ml of {self.get_formatted_ingredient('milk', drink, 'steamed milk') if drink['milk_steamed'] == True else self.get_formatted_ingredient('milk', drink)}. "
            if 'milk_foam' in drink:
                    ingredients += f"{drink['milk_foam']} ml of {self.get_formatted_ingredient('milk_foam', drink, 'steamed foam milk') if drink['foam_steamed'] == True else self.get_formatted_ingredient('milk_foam', drink, 'milk foam')}. "
            if 'chocolate_syrup' in drink:
                    ingredients += f"{drink['chocolate_syrup']} grams of {self.get_formatted_ingredient('chocolate_syrup',  drink, 'chocolate syrup')}. "
            if 'vanilla_ice_cream' in drink:
                    ingredients += f"{drink['vanilla_ice_cream']} grams of {self.get_formatted_ingredient('vanilla_ice_cream',  drink, 'vanilla ice cream')}. "
            if 'sugar' in drink:
                    ingredients += f"{drink['sugar']} grams of {self.get_formatted_ingredient('sugar',  drink)}. "

            print(f"{key.title()}, ingredients: {ingredients}\n")
        
        while True:
            choice = input("Please select the drink you're craving: ").lower()
            if choice not in self.coffee_recipes:
                continue
            else:
                return choice
        
    
        
            
        