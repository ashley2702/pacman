import random 

class Maze:
    def __init__(self):
        self.layout = [
            "#############################",
            "#...............#...........#",
            "#.#####.#..##.#.#.##..#...###",
            "#.#   #.#   #.#.#.#...#.....#",
            "#.# # #.# ###.#.#.### #.# # #",
            "#.# # #.#...#.#.#.#...#.#.#.#",
            "#.# ###.#####.#.#.#####.###.#",
            "#.#.......#.......#.......#.#",
            "#.#####.#.#.###.#####.#####.#",
            "#.......#.#.#.....#.....#...#",
            "###.#####.#.#####.#.###.#.###",
            ".............................", 
            "###.#.###.#.#####.###.#.#####",
            "#.......#.#.....#.#...#.....#",
            "#.#.#####.#.#####.#.###.#####",
            "#.#.......#.......#.........#",
            "#.# #####.#.#.###.#####.### #",
            "#.#...#...#.#.#.....#.#...#.#",
            "#.###.#.###.#.###.###.#.###.#",
            "#...........#...........#...#",
            "#############################"
        ]

        self.layout = [list(row) for row in self.layout]
        self.fruit_positions = []

    def display(self):
        for row in self.layout:
            print("".join(row))

    def update_position(self, x, y, char):
        self.layout[y][x] = char

    def is_wall(self, x, y):
        return self.layout[y][x] == "#"

    def is_empty(self, x, y):
        return self.layout[y][x] == "."

    def is_dot(self, x, y):
        return self.layout[y][x] == "."

    def is_fruit(self, x, y):
        return self.layout[y][x] == "F"
    
    


    def place_fruit(self, x, y):
        """Place fruit on the maze and track the position."""
        self.layout[y][x] = "F"
        self.fruit_positions.append((x, y))

    def remove_fruit(self, x, y):
        """Remove fruit from the maze and update the fruit positions."""
        if (x, y) in self.fruit_positions:
            self.fruit_positions.remove((x, y))
        self.update_position(x, y, ".")

    def place_pacman(self, x, y):
        self.update_position(x, y, "P")

    def place_ghost(self, x, y):
        self.update_position(x, y, "G")

    def place_dot(self, x, y):
        self.update_position(x, y, ".")

    def spawn_fruits(self):
        """Spawns 2 fruits in random empty positions."""
        fruits_spawned = 0
        while fruits_spawned < 2:
            x = random.randint(1, len(self.layout[0]) - 2)
            y = random.randint(1, len(self.layout) - 2)
            # Ensure the position is not occupied by walls, Pac-Man, or ghosts
            if self.is_empty(x, y) and (x, y) not in self.fruit_positions:
                self.place_fruit(x, y)
                fruits_spawned += 1
                print(f"Fruit spawned at ({x}, {y})")  # Debug print to confirm fruit placement1
        
