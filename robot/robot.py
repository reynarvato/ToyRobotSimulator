class Table:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.max_x = width - 1
        self.max_y = height - 1

    def is_valid_position(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.is_placed = False
