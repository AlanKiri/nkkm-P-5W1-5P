class UI:
    move_selection_choices = ('black', 'red', 'green')
    
    def __init__(self):
        self.bet = None
        self.move = None
    
    def bet_selection(self):
        while True:
            try:
                bet = int(input('Please enter your bet: '))
            except ValueError:
                continue
            self.bet = bet
            break
            
    def move_selection(self):
        while True:
            try:
                choice = input('Please enter your move selection(green, black, red): ')
                if choice not in self.move_selection_choices:
                    raise ValueError    
                self.move = choice
            except ValueError:
                continue
            break
            
    def display_result(self, result):
        print(f"Your move was {self.move}")

        if result == 0:
            print(f'Sorry you lost your {self.bet}$')
        else:
            print(f"Roulette resulted in {self.move}, congrats.")
            print(f"You won {self.bet * result}")
            