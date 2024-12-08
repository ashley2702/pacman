class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0

    def move(self, direction, maze):
        new_x, new_y = self.x, self.y
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

    # Check if movement is valid
        if not maze.is_wall(new_x, new_y):
        # Clear old position
            maze.update_position(self.x, self.y, " ")
        
        # Update Pac-Man's position
            self.x, self.y = new_x, new_y

        # Check for dots and collect
            if maze.is_dot(self.x, self.y):
                self.collect_dot()
                maze.update_position(self.x, self.y, " ")  # Remove dot

        # Check for fruits and collect
            elif maze.is_fruit(self.x, self.y):
                print(f"Fruit detected at ({self.x}, {self.y})")  # Debug
                self.collect_fruit()
                maze.update_position(self.x, self.y, " ")  # Remove fruit

        # Place Pac-Man at the new position
            maze.place_pacman(self.x, self.y)

    def collect_dot(self):
        self.score += 10
        print(f"Dot collected! Score: {self.score}")  # Debug

    def collect_fruit(self):
        self.score += 100
        print(f"Fruit collected! Score: {self.score}")  # Debug


