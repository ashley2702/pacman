from PIL import Image, ImageTk

class PacMan:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.score = 0
        self.canvas = canvas  # Pass canvas to PacMan

        try:
           
            self.image = Image.open("pacman.png")  
            resized_image = self.image.resize((10, 10), Image.LANCZOS)  
            self.pacman_image = ImageTk.PhotoImage(resized_image)  
            print("Pac-Man image loaded successfully!")

            
            self.pacman_sprite = self.canvas.create_image(
                (self.x * 20) + 10, (self.y * 20) + 10, image=self.pacman_image, anchor="center"
            )
          
            self.canvas.image = self.pacman_image

        except Exception as e:
            print(f"Error loading image: {e}")
            self.pacman_image = None  
            self.pacman_sprite = None  

        if not self.pacman_image:
            print("Pac-Man image is not available!")

    def move(self, direction, maze):
        if self.pacman_sprite is None:
            print("Pac-Man image is not available. Cannot move.")
            return

        new_x, new_y = self.x, self.y

        # Handle movement logic
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        # Boundary teleportation logic
        if new_x < 0:  # Left boundary
            new_x = len(maze.layout[0]) - 8
        elif new_x >= len(maze.layout[0]) - 8:  # Right boundary
            new_x = 0

        # Check if movement is valid
        if not maze.is_wall(new_x, new_y):
            # Clear the old position
            maze.update_position(self.x, self.y, " ")

            # Update position of Pac-Man on the canvas
            self.x, self.y = new_x, new_y
            self.canvas.coords(self.pacman_sprite, (self.x * 20) + 10, (self.y * 20) + 10)  # Move Pac-Man image

            # Resize the image each time before moving (like your friend's approach)
            resized_image = self.image.resize((10, 10), Image.LANCZOS)  # Resize each time to 10x10
            self.pacman_image = ImageTk.PhotoImage(resized_image)  # Recreate the Tkinter image

            # Update the canvas with the resized image
            self.canvas.itemconfig(self.pacman_sprite, image=self.pacman_image)

            # Check for and collect dots
            if maze.is_dot(self.x, self.y):
                self.collect_dot()
                maze.update_position(self.x, self.y, " ")  # Remove dot from the maze

            # Check for and collect fruits
            elif maze.is_fruit(self.x, self.y):
                self.collect_fruit()
                maze.update_position(self.x, self.y, " ")  # Remove fruit from the maze

            # Place Pac-Man in the new position
            maze.place_pacman(self.x, self.y)

    def collect_dot(self):
        self.score += 10
        print(f"Dot collected! Score: {self.score}")

    def collect_fruit(self):
        self.score += 100
        print(f"Fruit collected! Score: {self.score}")
