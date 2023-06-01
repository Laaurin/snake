from helperClasses.Directions import Directions


class Snake:
    def __init__(self, head_x, head_y):
        self.head_x = head_x
        self.head_y = head_y
        self.tail = [[head_x, head_y]] * 200
        self.direction = Directions.DOWN

    def move(self):
        self.tail.insert(0, list((self.head_x, self.head_y)))
        self.tail.pop()

        if self.direction == Directions.UP:
            self.head_y -= 1

        elif self.direction == Directions.DOWN:
            self.head_y += 1

        elif self.direction == Directions.LEFT:
            self.head_x -= 1

        elif self.direction == Directions.RIGHT:
            self.head_x += 1

    def grow(self):
        self.tail.append(self.tail[-1])
