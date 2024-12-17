import tkinter as tk
from gui import PacManGUI
from maze import Maze
from pacman import PacMan
from ghost import Ghost
from menu import Menu
from timer import Timer
import random
import threading



def setup_game():
    # Initialize maze
    maze = Maze()

    # Initialize Pac-Man
    pacman = PacMan(1, 1)
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

    def spawn_fruits():
        while True:
            threading.Event().wait(5)  # Wait 10 seconds
            for _ in range(2):  # Spawn two fruits
                while True:
                    x = random.randint(1, len(maze.layout[0]) - 2)
                    y = random.randint(1, len(maze.layout) - 2)
                    if maze.is_empty(x, y):
                        maze.place_fruit(x, y)
                        break

    # Start a thread to spawn fruits
    fruit_thread = threading.Thread(target=spawn_fruits, daemon=True)
    fruit_thread.start()

    return maze, pacman, ghosts


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
        maze, pacman, ghosts = setup_game()
        gui.setup(maze, pacman, ghosts)

        # Timer
        timer = Timer(limit=60)
        timer.start()

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
            # Move ghosts
            for ghost in ghosts:
                ghost.move(maze)

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
