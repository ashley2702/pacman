class Maze:
    def __init__(self):
        self.layout = [
            "#############################",
            "#...............#...........#",
            "#.#####.#####.#.#.#####.#####",
            "#.#   #.#   #.#.#.#   #.#   #",
            "#.# # #.# ###.#.#.### #.# # #",
            "#.# # #.#   #.#.#.#   #.# # #",
            "#.# ###.#####.#.#.#####.### #",
            "#.#.......#.......#.......# #",
            "#.#####.#.#.###.#####.#####.#",
            "#.......#.#.#.....#.....#...#",
            "###.#####.#.#####.#.###.#.###",
            ".............................",
            "###.#.###.#.#####.###.#.#####",
            "#.......#.#.....#.#...#.....#",
            "#.#.#####.#.#####.#.###.#####",
            "#.#.......#.......#.......# #",
            "#.# #####.#.#.###.#####.### #",
            "#.#   #   #.#.#.....#.#   # #",
            "#.###.#.###.#.###.###.#.#####",
            "#...........#...........#...#",
            "#############################"
        ]


        self.layout = [list(row) for row in self.layout]

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
        self.layout[y][x] = "F"
        

    def place_pacman(self, x, y):
        self.update_position(x, y, "P")

    def place_ghost(self, x, y):
        self.update_position(x, y, "G")

    def place_dot(self, x, y):
        self.update_position(x, y, ".")

    
        
