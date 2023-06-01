import pygame
from config import *


class Visuals:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Spiel")
        self.snake_color = 'green'

    def draw_grid(self):
        pygame.draw.rect(self.screen, "brown", (OFFSET_HORIZONTAL, OFFSET_VERTICAL, PLAY_AREA_WIDTH + 2 * BORDER_WIDTH,
                                                PLAY_AREA_HEIGHT + 2 * BORDER_WIDTH))
        for i in range(PLAY_AREA_HEIGHT // BLOCK_SIZE):
            for j in range(PLAY_AREA_WIDTH // BLOCK_SIZE):
                color = "#006400" if (i+j)%2 == 0 else "#00FF00"
                color = 'black'
                pygame.draw.rect(self.screen, color, (OFFSET_HORIZONTAL + BORDER_WIDTH + j * BLOCK_SIZE, OFFSET_VERTICAL
                                                      + BORDER_WIDTH + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_end(self, x1, y1, x2, y2, color):
        prev_x, prev_y = x1, y1
        if prev_x == x2:
            if prev_y < y2:
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        OFFSET_HORIZONTAL + BORDER_WIDTH + x2 * BLOCK_SIZE + SNAKE_GAP,
                        OFFSET_VERTICAL + BORDER_WIDTH + y2 * BLOCK_SIZE,
                        SNAKE_SIZE,
                        SNAKE_SIZE
                    )
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        OFFSET_HORIZONTAL + BORDER_WIDTH + x2 * BLOCK_SIZE + SNAKE_GAP,
                        OFFSET_VERTICAL + BORDER_WIDTH + y2 * BLOCK_SIZE + SNAKE_GAP * 2,
                        SNAKE_SIZE,
                        SNAKE_SIZE
                    )
                )

        else:
            if prev_x < x2:
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        OFFSET_HORIZONTAL + BORDER_WIDTH + x2 * BLOCK_SIZE,
                        OFFSET_VERTICAL + BORDER_WIDTH + y2 * BLOCK_SIZE + SNAKE_GAP,
                        SNAKE_SIZE,
                        SNAKE_SIZE
                    )
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        OFFSET_HORIZONTAL + BORDER_WIDTH + x2 * BLOCK_SIZE + SNAKE_GAP  * 2,
                        OFFSET_VERTICAL + BORDER_WIDTH + y2 * BLOCK_SIZE + SNAKE_GAP,
                        SNAKE_SIZE,
                        SNAKE_SIZE
                    )
                )

    def draw_bottom_left_corner(self, square_x, square_y):
        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE + SNAKE_GAP,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE,
                SNAKE_SIZE,
                BLOCK_SIZE - SNAKE_GAP
            )
        )

        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE + SNAKE_GAP + SNAKE_SIZE,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE + SNAKE_GAP,
                SNAKE_GAP,
                SNAKE_SIZE
            )
        )

    def draw_bottom_right_corner(self, square_x, square_y):
        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE + SNAKE_GAP,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE,
                SNAKE_SIZE,
                BLOCK_SIZE - SNAKE_GAP
            )
        )

        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE + SNAKE_GAP,
                SNAKE_GAP,
                SNAKE_SIZE
            )
        )

    def draw_top_left_corner(self, square_x, square_y):
        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE + SNAKE_GAP,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE + SNAKE_GAP,
                SNAKE_SIZE,
                BLOCK_SIZE - SNAKE_GAP
            )
        )

        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE + SNAKE_GAP + SNAKE_SIZE,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE + SNAKE_GAP,
                SNAKE_GAP,
                SNAKE_SIZE
            )
        )

    def draw_top_right_corner(self, square_x, square_y):
        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE + SNAKE_GAP,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE + SNAKE_GAP,
                SNAKE_SIZE,
                BLOCK_SIZE - SNAKE_GAP
            )
        )

        pygame.draw.rect(
            self.screen,
            self.snake_color,
            (
                OFFSET_HORIZONTAL + BORDER_WIDTH + square_x * BLOCK_SIZE,
                OFFSET_VERTICAL + BORDER_WIDTH + square_y * BLOCK_SIZE + SNAKE_GAP,
                SNAKE_GAP,
                SNAKE_SIZE
            )
        )

    def set_corner(self, prev_x, prev_y, cur_x, cur_y, next_x, next_y):
        if (prev_x < cur_x and next_y > cur_y) or (prev_x > next_x and cur_y < prev_y):
            self.draw_top_right_corner(cur_x, cur_y)

        elif (prev_x > cur_x and next_y > cur_y) or (prev_x < next_x and cur_y < prev_y):
            self.draw_top_left_corner(cur_x, cur_y)

        elif (prev_x > cur_x and next_y < cur_y) or (prev_x < next_x and cur_y > prev_y):
            self.draw_bottom_left_corner(cur_x, cur_y)

        elif (cur_x > next_x and cur_y > prev_y) or (prev_x < next_x and cur_y > next_y):
            self.draw_bottom_right_corner(cur_x, cur_y)

    def draw_segment(self, prev_pos, cur_pos, next_pos):
        prev_x, prev_y = prev_pos
        cur_x, cur_y = cur_pos
        next_x, next_y = next_pos

        square_x = OFFSET_HORIZONTAL + BORDER_WIDTH + cur_x * BLOCK_SIZE
        square_y = OFFSET_VERTICAL + BORDER_WIDTH + cur_y * BLOCK_SIZE

        if prev_y == next_y:
            pygame.draw.rect(
                self.screen,
                self.snake_color,
                (
                    square_x,
                    square_y + SNAKE_GAP,
                    BLOCK_SIZE,
                    SNAKE_SIZE
                )
            )

        elif prev_x == next_x:
            pygame.draw.rect(
                self.screen,
                self.snake_color,
                (
                    square_x + SNAKE_GAP,
                    square_y,
                    SNAKE_SIZE,
                    BLOCK_SIZE
                )
            )

        self.set_corner(prev_x, prev_y, cur_x, cur_y, next_x, next_y)

    def draw_snake(self, snake):
        # draw head

        self.draw_end(snake.tail[0][0], snake.tail[0][1], snake.head_x, snake.head_y, 'green')

        self.draw_segment(snake.tail[1], snake.tail[0], [snake.head_x, snake.head_y])

        for i in range(1, len(snake.tail) - 1):
            self.draw_segment(snake.tail[i+1], snake.tail[i], snake.tail[i-1])

        # draw tail
        self.draw_end(snake.tail[-1][0], snake.tail[-1][1], snake.tail[-2][0], snake.tail[-2][1], 'green')

    def draw_fruit(self, fruit):
        color = 'purple'
        pygame.draw.rect(self.screen, color, (OFFSET_HORIZONTAL + BORDER_WIDTH + fruit.fruit_x * BLOCK_SIZE,
                         OFFSET_VERTICAL + BORDER_WIDTH + fruit.fruit_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 3)


