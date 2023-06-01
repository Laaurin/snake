import pygame
from config import *
from game.Fruit import Fruit
from game.Snake import Snake
from game.Bot import Bot
from helperClasses.Visuals import Visuals
from helperClasses.Directions import Directions


class Game:
    def __init__(self):
        self.visuals = Visuals()
        self.snake = Snake(0, 0)
        self.fruit = Fruit()
        self.bot = Bot()
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.playing = True
        #self.bot.create_path(self.snake, self.fruit)

    def run(self):
        while self.is_running:
            self.handle_events()

            while self.playing:
                self.handle_events()
                self.snake.direction = self.bot.cycle[self.snake.head_y][self.snake.head_x]
                self.snake.move()
                if self.handle_collision():
                    #self.bot.create_path(self.snake, self.fruit)
                    pass
                if self.game_over():
                    self.playing = False
                    break
                self.visuals.draw_grid()
                self.visuals.draw_snake(self.snake)
                self.visuals.draw_fruit(self.fruit)
                pygame.display.update()

                self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != Directions.DOWN:
                    self.snake.direction = Directions.UP
                elif event.key == pygame.K_DOWN and self.snake.direction != Directions.UP:
                    self.snake.direction = Directions.DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != Directions.RIGHT:
                    self.snake.direction = Directions.LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != Directions.LEFT:
                    self.snake.direction = Directions.RIGHT

    def handle_collision(self):
        if (self.fruit.fruit_x, self.fruit.fruit_y) == (self.snake.head_x, self.snake.head_y):
            self.snake.grow()
            self.fruit.new_pos(self.snake)
            return True
        return False

    def game_over(self):
        if [self.snake.head_x, self.snake.head_y] in self.snake.tail:
            return True

        if not 0 <= self.snake.head_x <= PLAY_AREA_WIDTH//BLOCK_SIZE:
            return True

        if not 0 <= self.snake.head_y <= PLAY_AREA_HEIGHT//BLOCK_SIZE:
            return True

        return False

    def get_direction_from_path(self):
        return self.bot.path.pop(0)
