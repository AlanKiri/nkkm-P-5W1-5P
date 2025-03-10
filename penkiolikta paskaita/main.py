from game import Game
from time import sleep

if __name__ == '__main__':
    
    while True:
        game = Game()
        game.bet_selection()
        game.move_selection()
        result = game.start()
        print(result)
        sleep(5)
        game.display_result(result)
        sleep(5)
