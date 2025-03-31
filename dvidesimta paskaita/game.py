from turtle import Turtle, Screen
from time import sleep
from food import Food
from snake import Snake
import const

class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(const.WIDTH+24, const.HEIGHT+24)
        self.screen.tracer(0)
        
        self.food = []
        self.init_food()
        
        self.grid = Turtle()
        self.init_grid()
        
        self.snake = Snake()
        self.listen_keyboard()
        self.start()
        
    def start(self):
        while True:
            self.screen.update()
            self.snake.move()
            sleep(0.3)
        
    
    def listen_keyboard(self):
        self.screen.listen()
        # UP
        self.screen.onkeypress(self.snake.rotate_top, 'w')
        self.screen.onkeypress(self.snake.rotate_top, 'Up')
        # Bottom
        self.screen.onkeypress(self.snake.rotate_bottom, 's')
        self.screen.onkeypress(self.snake.rotate_bottom, 'Down')
        # Left
        self.screen.onkeypress(self.snake.rotate_left, 'a')
        self.screen.onkeypress(self.snake.rotate_left, 'Left')
        # Right
        self.screen.onkeypress(self.snake.rotate_right, 'd')
        self.screen.onkeypress(self.snake.rotate_right, 'Right')
        # Escape
        self.screen.onkeypress(self.screen.bye, 'Escape')
        
    def init_food(self):
        for _ in range(3):
            new_food = Food()
            new_food.render()
            self.food.append(new_food)
        
        
    def init_grid(self):
        self.grid.hideturtle()
        self.grid.speed(0)
        self.draw_grid()
        
    def draw_grid(self):
        # Horizontal
        self.grid.seth(0)
        for index in range(int(const.HEIGHT / const.GRID_SIZE)+1):
            teleport_x, teleport_y = const.X[0], (const.Y[1] - (index * const.GRID_SIZE))
            self.grid.teleport(teleport_x, teleport_y)
            self.grid.forward(1000)
        
        # Vertical
        self.grid.seth(90)
        for index in range(int(const.WIDTH / const.GRID_SIZE)+1):
            teleport_x, teleport_y = (const.X[1] - (index * const.GRID_SIZE)), const.Y[0]
            self.grid.teleport(teleport_x, teleport_y)
            self.grid.forward(1000)
            
        self.screen.update()
            
            
    
    