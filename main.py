import tkinter as tk
from gui import PacManGUI
from maze import Maze
from pacman import PacMan
from ghost import Ghost
from menu import Menu
from timer import Timer
import random


def setup_game(gui):
    # Initialize maze
    maze = Maze()

    # Initialize Pac-Man
    pacman = PacMan(1, 1, gui.canvas)  # Pass the canvas from gui to PacMan

    maze.place_pacman(pacman.x, pacman.y)

    # Initialize ghosts
    ghosts = [
        Ghost(10, 3, "1"),
        Ghost(15, 5, "2"),
        Ghost(3, 6, "3")
    ]
    for ghost in ghosts:
        maze.place_ghost(ghost.x, ghost.y)

    # Add dots
    for y in range(len(maze.layout)):
        for x in range(len(maze.layout[y])):
            if maze.is_empty(x, y):
                maze.place_dot(x, y)

    return maze, pacman, ghosts


def spawn_fruits(maze):
    """Spawn two fruits after a predefined time."""
    fruits_spawned = 0
    while fruits_spawned < 2:
        x = random.randint(1, len(maze.layout[0]) - 2)
        y = random.randint(1, len(maze.layout) - 2)
        if maze.is_empty(x, y):  # Ensure no wall, Pac-Man, or ghost is at this position
            maze.place_fruit(x, y)
            fruits_spawned += 1


def main():
    # Menu for game start
    menu = Menu()
    menu.display()
    choice = menu.select_option()

    if choice == "start":
        # Initialize GUI
        root = tk.Tk()
        gui = PacManGUI(root)

        # Game setup
        maze, pacman, ghosts = setup_game(gui)
        gui.setup(maze, pacman, ghosts)

        # Timer
        timer = Timer(limit=60)
        timer.start()

        # Slower ghost movement (e.g., move every 500ms)
        def move_ghosts():
            for ghost in ghosts:
                ghost.move(maze)
            root.after(200, move_ghosts)  # Schedule next move after 500ms

        # Start the ghost movement loop
        root.after(200, move_ghosts)

        # Function to handle user input
        def handle_keypress(event):
            direction_map = {
                "Up": "up",
                "Down": "down",
                "Left": "left",
                "Right": "right",
            }
            direction = direction_map.get(event.keysym)
            if direction:
                pacman.move(direction, maze)

        # Bind keys to Pac-Man movement
        root.bind("<KeyPress>", handle_keypress)

        def game_loop():
            # Update GUI
            gui.update_maze()
            gui.show_score(pacman.score)
            gui.show_timer(int(timer.remaining_time()))

            # Check timer
            if timer.remaining_time() <= 0:
                gui.update_maze()
                print("Time's up! Game Over!")
                gui.canvas.create_text(
                    200, 200, text="Time's up! Game Over!", fill="white", font=("Arial", 20)
                )
                root.after(3000, root.quit)
                return

            # Check collision with ghosts
            for ghost in ghosts:
                if pacman.x == ghost.x and pacman.y == ghost.y:
                    gui.update_maze()
                    print("Game Over! Pac-Man was caught by a ghost!")
                    gui.canvas.create_text(
                        200, 200, text="Game Over! Caught by a Ghost!", fill="red", font=("Arial", 20)
                    )
                    root.after(3000, root.quit)
                    return

            # Check win condition
            if all(
                not maze.is_dot(x, y)
                for y in range(len(maze.layout))
                for x in range(len(maze.layout[y]))
            ):
                gui.update_maze()
                print("You Win!")
                gui.canvas.create_text(
                    200, 200, text="You Win!", fill="green", font=("Arial", 20)
                )
                root.after(3000, root.quit)
                return

            # Schedule the next update (100ms)
            root.after(100, game_loop)

        # Start the game loop
        game_loop()
        root.mainloop()


if __name__ == "__main__":
    main()
