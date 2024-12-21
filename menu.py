import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


class Menu:
    def __init__(self, root, gui, start_game_callback):
        self.root = root
        self.gui = gui
        self.start_game_callback = start_game_callback

    def display_main_menu(self):
        # Clear the canvas (if anything is already drawn)
        self.gui.canvas.delete("all")

        # Ensure the canvas is fully black without borders
        self.gui.canvas.config(bg="black", highlightthickness=0)

        # Create a list to track buttons so we can clean them up later
        self.menu_buttons = []

        try:
            # Load and resize the Pac-Man logo image
            self.image = Image.open("pacman_logo.png")  # Replace with your image path
            self.original_image = self.image.resize((500, 400), Image.LANCZOS)
            self.pacman_logo = ImageTk.PhotoImage(self.original_image)

            # Draw the logo directly on the canvas
            self.gui.canvas.create_image(300, 150, image=self.pacman_logo, anchor="center")  # Center the logo
        except Exception as e:
            # Fallback to text if the image fails to load
            print(f"Error loading Pac-Man logo: {e}")
            self.gui.canvas.create_text(
                300, 150, text="PAC-MAN", fill="yellow", font=("Courier", 40, "bold")
            )

        # Add buttons below the canvas
        start_button = tk.Button(
            self.gui.canvas,
            text="Start Game",
            font=("Courier", 18, "bold"),
            height=2,
            relief="ridge",  # Sets the border style (e.g., flat, ridge, groove, etc.)
            bd=0.5,            # Sets the border thickness to 5
            highlightbackground="yellow",  # Color of the border when not focused
            highlightcolor="red",        # Color of the border when focused
            highlightthickness=2,
            command=lambda: [self.clear_menu(), self.start_game_callback()]
        )
        self.gui.canvas.create_window(290, 300, window=start_button)
        self.menu_buttons.append(start_button)

        instructions_button = tk.Button(
            self.gui.canvas,
            text="Instructions",
            font=("Courier", 14,"bold"),
            height=2,
            relief="ridge",  # Sets the border style (e.g., flat, ridge, groove, etc.)
            bd=0.5,            # Sets the border thickness to 5
            highlightbackground="red",  # Color of the border when not focused
            highlightcolor="red",        # Color of the border when focused
            highlightthickness=2,
            command=lambda: messagebox.showinfo(
                "Instructions", "Use arrow keys to move.\nAvoid the ghosts and collect all dots!"
            )
        )
        self.gui.canvas.create_window(290, 350, window=instructions_button)
        self.menu_buttons.append(instructions_button)

        exit_button = tk.Button(
            self.gui.canvas,
            text="Exit",
            font=("Courier", 14,"bold"),
            height=2,
            relief="ridge",  # Sets the border style (e.g., flat, ridge, groove, etc.)
            bd=0.5,            # Sets the border thickness to 5
            highlightbackground="blue",  # Color of the border when not focused
            highlightcolor="red",        # Color of the border when focused
            highlightthickness=2,
            command=self.root.quit
        )
        self.gui.canvas.create_window(290, 400, window=exit_button)
        self.menu_buttons.append(exit_button)

    def clear_menu(self):
        self.gui.canvas.delete()  # Clear everything on the canvas

        # Explicitly destroy all buttons
        for button in self.menu_buttons:
            button.destroy()
        self.menu_buttons.clear()  # Clear the list of buttons
