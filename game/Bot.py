from config import *
from helperClasses.Directions import Directions


class Bot:
    def __init__(self):
        self.cycle = [[None for _ in range(PLAY_AREA_WIDTH//BLOCK_SIZE)] for _ in range(PLAY_AREA_HEIGHT//BLOCK_SIZE)]
        self.create_cycle()
        self.path = []

    def create_cycle(self):
        width = PLAY_AREA_WIDTH//BLOCK_SIZE
        height = PLAY_AREA_HEIGHT//BLOCK_SIZE
        for i in range(height):
            for j in range(width):
                if j == 0:
                    if i != height - 1:
                        self.cycle[i][j] = Directions.DOWN
                    else:
                        self.cycle[i][j] = Directions.RIGHT

                elif i % 2 == 0:
                    if j == 1 and i != 0:
                        self.cycle[i][j] = Directions.UP
                    else:
                        self.cycle[i][j] = Directions.LEFT

                else:
                    if j == width - 1:
                        self.cycle[i][j] = Directions.UP
                    else:
                        self.cycle[i][j] = Directions.RIGHT

    def follow_cycle(self, x, y):
        direction = self.cycle[y][x]
        if direction == Directions.UP:
            return y-1, x
        if direction == Directions.DOWN:
            return y+1, x
        if direction == Directions.LEFT:
            return y, x-1
        if direction == Directions.RIGHT:
            return y, x+1

    def create_path(self, snake, fruit):
        x, y = snake.head_x, snake.head_y
        self.path = []

        while True:
            print(self.path)
            if (x, y) == (fruit.fruit_x, fruit.fruit_y):
                return

            if x == 0 and y > fruit.fruit_y:
                self.path.append(Directions.RIGHT)
                x += 1

            else:
                self.path.append(self.cycle[y][x])
                x, y = self.follow_cycle(x, y)

