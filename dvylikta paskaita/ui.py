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
        return formatted_ingredient if self.check_ingredient_stock(ingredient, required_stock) else self.underscore(formatted_ingredient)
        
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
            
            for ingredient, amount in self.ingredients.items():
                if ingredient in drink:
                    steamed_name = f"{ingredient}_steamed"
                    if steamed_name in self.ingredients:
                        ingredients += f"{drink[ingredient]} ml/g of {self.get_formatted_ingredient(ingredient, drink, f'steamed {ingredient.title().replace('_', ' ')}') if drink[steamed_name] == True else self.get_formatted_ingredient(ingredient, drink, ingredient.title().replace('_', ' '))}."
                    else: 
                        ingredients += f"{drink[ingredient]} ml/g of {self.get_formatted_ingredient(ingredient, drink, ingredient.title().replace('_', ' '))} "

            print(f"{key.title()}, ingredients: {ingredients}\n")
        
        while True:
            choice = input("Please select the drink you're craving: ").lower()
            if choice not in self.coffee_recipes:
                continue
            else:
                return choice
            
    def drink_details_menu_selection(self, drink:str):
        print(f"You selected {drink.title()}")
        drink_in_stock = self.check_drink_stock(drink)
        print('Stock is ok. Enter anything to proceed.' if drink_in_stock else self.underscore('Stock is not okay. Sorry, but we cannot proceed without required ingredients. Please press enter to return into main menu.'))
        input('')
        return drink_in_stock
    
    def restock_menu_selection(self):
        print("You want to restock, don't you?")
        
        for ingredient, stock in self.ingredients.items():
            print(f"{ingredient.title().replace('_', ' ')}, current stock {stock} g/ml")
            
        print('Please select products you want to order.')
        
        choice = list(map(lambda ingredient: ingredient.lower(), input().split()))
        
        return choice