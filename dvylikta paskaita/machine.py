from ui import UI
from sys import exit
from time import sleep

class Machine(UI):
    def __init__(self):
        super().__init__()
        
    def run(self):
        self.clear()
        self.display_stock()
        choice = self.display_main_menu_selection()
        
        match choice:
            case '1':
                self.clear()
                self.coffee_machine_header()
                drink = self.drink_menu_selection()
                ingredients = self.coffee_recipes[drink]
                # Drink got selected
                self.clear()
                self.coffee_machine_header()
                stock_ok = self.drink_details_menu_selection(drink)
                if stock_ok:
                    self.brew_coffee(drink)
            case '2':
                self.clear()
                self.coffee_machine_header()
                ingredients = self.restock_menu_selection()
                # Ingredients to restock got selected
                self.clear()
                self.coffee_machine_header()
                for ingredient in ingredients:
                    arrived_stock = self.order_ingredients(ingredient)
                    print(f"{arrived_stock} units of {ingredient} arrived.")
                print('Press enter when you want to exit this menu.')
                input()
            case 'e' | 'exit':
                self.clear()
                self.coffee_machine_header()
                print('Sorry to see you go!')
                exit()
                
    def brew_coffee(self, drink:str):
        drink_ingredients = self.coffee_recipes[drink]
        self.clear()
        print(f"Preparing {drink.title()}... Please wait.")
        
        if self.ingredients['coffee_ground'] < drink_ingredients['coffee_ground']:
            self.grind_coffee_beans(drink_ingredients['coffee_ground'])
        
        sleep(1)
        print('Loading ingredients')
        sleep(2)
        print(f"Brewing {drink.title()}")
        sleep(2)
        
        if 'milk' in self.coffee_recipes[drink]:
            print('Steaming milk')
            sleep(2)
            
        if 'milk_foam' in drink_ingredients:
            print('Steaming milk foam')
            sleep(2)        
            
        print('Finalizing')
        sleep(2)
        
        self.remove_used_ingredients(drink_ingredients)
        
        self.clear()
        print(f"{drink.title()} is ready! Enjoy your drink!")
        print('Press enter when you want to exit this menu.')
        input()