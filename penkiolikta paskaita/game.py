from ui import UI
from random import randint

class Game(UI):
    def __init__(self):
        super().__init__()
       
    def start(self):
        number = randint(0, 36)
        print(number)
        
        if number == 0 and self.move == 'green':
            return 14
        elif number % 2 == 0 and self.move == 'black':
            return 2
        elif number % 2 == 1 and self.move == 'red':
            return 2
        else:
            return 0
    
    