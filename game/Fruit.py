from config import *
import random
class Fruit:
    def __init__(self):
        self.fruit_x = 20
        self.fruit_y = 20

    def new_pos(self, snake):
        possible_positions = []
        for x in range(PLAY_AREA_WIDTH//BLOCK_SIZE):
            for y in range(PLAY_AREA_HEIGHT//BLOCK_SIZE):
                if [x, y] not in snake.tail and [x, y] != (snake.head_x, snake.head_y):
                    possible_positions.append([x, y])

        # Wähle eine zufällige Position aus den möglichen Positionen
        if possible_positions:
            self.fruit_x, self.fruit_y = random.choice(possible_positions)
        else:
            # Wenn keine möglichen Positionen vorhanden sind, gibt es keine freien Plätze mehr
            return None