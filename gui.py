import tkinter as tk

class PacManGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pac-Man Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.maze = None
        self.pacman = None
        self.ghosts = []
        self.pacman_image = None

        # Load the Pac-Man image
        self.pacman_image = tk.PhotoImage(file="pacman.png")

    def setup(self, maze, pacman, ghosts):
        self.maze = maze
        self.pacman = pacman
        self.ghosts = ghosts
        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.maze.layout):
            for x, cell in enumerate(row):
                if cell == "#":
                    self.canvas.create_rectangle(
                        x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="blue"
                    )
                elif cell == ".":
                    self.canvas.create_oval(
                        x * 20 + 7, y * 20 + 7, x * 20 + 13, y * 20 + 13, fill="white"
                    )
                elif cell == "P":
                    self.canvas.create_image(
                        (x + 0.5) * 20, (y + 0.5) * 20, image=self.pacman_image
                    )
                elif cell == "G":
                    self.canvas.create_oval(
                        x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="red"
                    )
                elif cell == "F":
                    self.canvas.create_rectangle(
                        x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green"
                    )

    def update_maze(self):
        self.draw_maze()

    def show_score(self, score):
        self.canvas.create_text(
            200, 10, text=f"Score: {score}", fill="white", font=("Arial", 16)
        )

    def show_timer(self, time_left):
        self.canvas.create_text(
            200, 30, text=f"Time Left: {time_left}s", fill="white", font=("Arial", 16)
        )

