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
                stock_ok = None
                
            case '2':
                pass
            case 'e' | 'exit':
                self.clear()
                self.coffee_machine_header()
                print('Sorry to see you go!')
                exit()