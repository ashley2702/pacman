from PIL import Image, ImageTk

class PacMan:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.score = 0
        self.canvas = canvas
        self.original_image = None

        try:
            self.image = Image.open("pacman.png")  # Loads the Pac-Man image called pacman.png and then resize it
            self.original_image = self.image.resize((20, 20), Image.LANCZOS) 
            self.pacman_image = ImageTk.PhotoImage(self.original_image)  
            print("Pac-Man image loaded successfully!")
            self.pacman_sprite = self.canvas.create_image(
                (self.x * 20) + 10, (self.y * 20) + 10, image=self.pacman_image, anchor="center"
            )

        except Exception as e:
            print(f"Error loading image: {e}")
            self.pacman_image = None
            self.pacman_sprite = None

    def rotate_image(self, angle):
        if self.original_image:  
            if angle == 180:  
                flipped_image = self.original_image.transpose(Image.FLIP_LEFT_RIGHT)
                self.pacman_image = ImageTk.PhotoImage(flipped_image)
            else:
                rotated_image = self.original_image.rotate(angle)
                self.pacman_image = ImageTk.PhotoImage(rotated_image)
                
            self.canvas.itemconfig(self.pacman_sprite, image=self.pacman_image)

    def move(self, direction, maze):
        if self.pacman_sprite is None:
            print("Pac-Man image is not available. Cannot move.")
            return

        new_x, new_y = self.x, self.y

        if direction == "up":
            new_y -= 1
            self.rotate_image(90) 
        elif direction == "down":
            new_y += 1
            self.rotate_image(270)  
        elif direction == "left":
            new_x -= 1
            self.rotate_image(180) 
        elif direction == "right":
            new_x += 1
            self.rotate_image(0) 

        if new_x < 0:  
            new_x = len(maze.layout[0]) - 1
        elif new_x >= len(maze.layout[0]) - 0: 
            new_x = 0


        if not maze.is_wall(new_x, new_y):
            maze.update_position(self.x, self.y, " ") 
            self.x, self.y = new_x, new_y
            self.canvas.coords(self.pacman_sprite, (self.x * 20) + 10, (self.y * 20) + 10)

            if maze.is_dot(self.x, self.y):
                self.collect_dot()
                maze.update_position(self.x, self.y, " ")
            elif maze.is_fruit(self.x, self.y):
                self.collect_fruit(maze)
                maze.update_position(self.x, self.y, " ")

            maze.place_pacman(self.x, self.y)

    def collect_dot(self):
        self.score += 10

    def collect_fruit(self, maze):
        self.score += 100

        # Remove the fruit from the maze when eaten. 
        maze.remove_fruit(self.x, self.y)
