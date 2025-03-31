WIDTH = 1000
X = list(map(int, [-abs(WIDTH/2), abs(WIDTH/2)]))

HEIGHT = 1000
Y = list(map(int, [-abs(HEIGHT/2), abs(HEIGHT/2)]))

GRID_SIZE = 50

ENTITY_SIZE = GRID_SIZE / 25

STARTING_SNAKE_SIZE = 3

def adapt_grid(number:int):
    return number + GRID_SIZE / 2

