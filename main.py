import tkinter as tk
from gui import PacManGUI
from maze import Maze
from pacman import PacMan
from ghost import Ghost
from timer import Timer
from menu import Menu



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


def main():
    # Initialize GUI
    root = tk.Tk()
    root.geometry("580x500")
    gui = PacManGUI(root)

    def start_game():
        # Game setup
        maze, pacman, ghosts = setup_game(gui)
        gui.setup(maze, pacman, ghosts)

        # Timer
        timer = Timer(limit=60)
        timer.start()

        # Function to spawn fruits after 10 seconds
        def spawn_fruits():
            maze.spawn_fruits()  # Call the spawn_fruits() method to place 2 fruits
            print("Fruits spawned!")  # Debugging message

        # Spawn fruits after 10 seconds
        root.after(10000, spawn_fruits)  # Call spawn_fruits() after 10 seconds

        # Slower ghost movement (e.g., move every 200ms)
        def move_ghosts():
            for ghost in ghosts:
                ghost.move(maze)
            root.after(200, move_ghosts)  # Schedule next move after 200ms

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
                300, 440, text=f"FINAL SCORE: {pacman.score}", fill="#FFFFFF", font=("Courier", 20, "bold")
                )

                # Shadow Effect - Red Glow
                gui.canvas.create_text(
                    300, 475, text="TIME'S UP! GAME OVER!", fill="#FF0000", font=("Courier", 28, "bold")
                )
                # Top Layer - White Text
                gui.canvas.create_text(
                    300, 475, text="TIME'S UP! GAME OVER!", fill="#FFFFFF", font=("Courier", 28, "bold")
                )
                root.after(3000, lambda: menu.display_main_menu())
                return

            # Check collision with ghosts
            for ghost in ghosts:
                if pacman.x == ghost.x and pacman.y == ghost.y:
                    gui.update_maze()
                    print("Game Over! Pac-Man was caught by a ghost!")

                    gui.canvas.create_text(
                    300, 440, text=f"FINAL SCORE: {pacman.score}", fill="#FFFFFF", font=("Courier", 20, "bold")
                    )

                    # Shadow Effect - Red Glow
                    gui.canvas.create_text(
                        300, 475, text="GAME OVER! CAUGHT BY A GHOST!", fill="#FF0000", font=("Courier", 28, "bold")
                    )
                    # Top Layer - White Text
                    gui.canvas.create_text(
                        300, 475, text="GAME OVER! CAUGHT BY A GHOST!", fill="#FFFFFF", font=("Courier", 28, "bold")
                    )

                    # Close the game after 3 seconds
                    root.after(3000, lambda: menu.display_main_menu())
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
                300, 440, text=f"FINAL SCORE: {pacman.score}", fill="#FFD700", font=("Courier", 20, "bold")
                
                )
                # Shadow Effect - Yellow Glow
                gui.canvas.create_text(
                    300, 475, text="YOU WIN!", fill="#FFD700", font=("Courier", 28, "bold")
                )
                # Top Layer - White Text
                gui.canvas.create_text(
                    300, 475, text="YOU WIN!", fill="#FFFFFF", font=("Courier", 28, "bold")
                )

                # Close the game after 3 seconds
                root.after(3000, lambda: menu.display_main_menu())
                return

            # Schedule the next update (100ms)
            root.after(100, game_loop)

        # Start the game loop
        game_loop()

    # Create the menu
    menu = Menu(root, gui, start_game)

    # Display the main menu on startup
    menu.display_main_menu()

    root.mainloop()


if __name__ == "__main__":
    main()
