from PIL import Image, ImageTk

class PacMan:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.score = 0
        self.canvas = canvas
        self.original_image = None

        try:
            # Load Pac-Man image
            self.image = Image.open("pacman.png")  # Ensure the path is correct
            self.original_image = self.image.resize((20, 20), Image.LANCZOS)  # Resize to 20x20
            self.pacman_image = ImageTk.PhotoImage(self.original_image)  # Convert to Tkinter image format
            print("Pac-Man image loaded successfully!")

            # Create Pac-Man sprite on the canvas
            self.pacman_sprite = self.canvas.create_image(
                (self.x * 20) + 10, (self.y * 20) + 10, image=self.pacman_image, anchor="center"
            )

        except Exception as e:
            print(f"Error loading image: {e}")
            self.pacman_image = None
            self.pacman_sprite = None

    def rotate_image(self, angle):
        """Rotate the original image by the given angle and update Pac-Man's sprite."""
        if self.original_image:  # Ensure the original image is loaded
            rotated_image = self.original_image.rotate(angle)  # Rotate the image
            self.pacman_image = ImageTk.PhotoImage(rotated_image)  # Convert rotated image to Tkinter format
            self.canvas.itemconfig(self.pacman_sprite, image=self.pacman_image)  # Update the canvas image

    def move(self, direction, maze):
        if self.pacman_sprite is None:
            print("Pac-Man image is not available. Cannot move.")
            return

        new_x, new_y = self.x, self.y

        # Handle movement logic and rotate image
        if direction == "up":
            new_y -= 1
            self.rotate_image(90)  # Face upward
        elif direction == "down":
            new_y += 1
            self.rotate_image(270)  # Face downward
        elif direction == "left":
            new_x -= 1
            self.rotate_image(180)  # Face left
        elif direction == "right":
            new_x += 1
            self.rotate_image(0)  # Face right (default)

        # Boundary teleportation logic
        if new_x < 0:  # Left boundary
            new_x = len(maze.layout[0]) - 1
        elif new_x >= len(maze.layout[0]) - 1:  # Right boundary
            new_x = 0

        # Check if movement is valid
        if not maze.is_wall(new_x, new_y):
            maze.update_position(self.x, self.y, " ")  # Clear old position
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
        print(f"Dot collected! Score: {self.score}")

    def collect_fruit(self, maze):
        self.score += 100
        print(f"Fruit collected! Score: {self.score}")

        # Remove the fruit from the maze
        maze.remove_fruit(self.x, self.y)
