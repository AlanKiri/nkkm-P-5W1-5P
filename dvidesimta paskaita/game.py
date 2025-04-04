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
            self.check_collisions()
            self.screen.update()
            self.snake.move()
            sleep(0.3)
            
    def check_collisions(self):
        current_x, current_y = self.snake.pos()
        
        if self.check_border_collisions(current_x, current_y):
            self.screen.bye()
            
        food_collision_index = self.check_food_collisions(current_x, current_y)
        
        if food_collision_index != -1:
            self.snake.queue += 1
            self.replace_food(food_collision_index)
            
        if self.check_snake_tail_collisions(*self.snake.pos()):
            self.screen.bye()
            
            
    def check_border_collisions(self, x, y):
        result = False
        
        if x < const.X[0] or x > const.X[1]:
            result = True
        elif y < const.Y[0] or y > const.Y[1]:
            result = True
        return result
    
    def check_food_collisions(self, x, y):
        for index, food in enumerate(self.food):
            if (round(x), round(y)) == (round(food.pos()[0]), round(food.pos()[1])):
                return index
        return -1
    
    def check_snake_tail_collisions(self, x, y):
        result = False

        for path in self.snake.paths:
            if (round(x), round(y)) == (round(path.pos()[0]), round(path.pos()[1])):
                result = True
        return result

    
    def check_all_collisions(self, x, y):
        cords = (x, y)
        result = False
        
        if self.check_border_collisions(*cords):
            result = True
        if self.check_food_collisions(*cords) != -1:
            result = True
        if  self.check_snake_tail_collisions(*cords):
            result = True
            
        return result
        
    
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
            
    def replace_food(self, index):
        self.food[index].sabotage()
        del self.food[index]
        while True:
            new_food = Food()
            if not self.check_all_collisions(*new_food.pos()):
                new_food.render()
                self.food.append(new_food)
                break
        
        
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
            
            
    
    