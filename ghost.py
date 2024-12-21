import random

class Ghost:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def move(self, maze):
        directions = ["up", "down", "left", "right"]
        random.shuffle(directions)
        for direction in directions:
            new_x, new_y = self.x, self.y
            if direction == "up":
                new_y -= 1
            elif direction == "down":
                new_y += 1
            elif direction == "left":
                new_x -= 1
            elif direction == "right":
                new_x += 1

            if not maze.is_wall(new_x, new_y):
                maze.update_position(self.x, self.y, ".")
                self.x, self.y = new_x, new_y
                maze.place_ghost(self.x, self.y)
                break
