import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def pulsate_button(button, color1, color2):
        current_color = button.cget("highlightbackground")
        new_color = color1 if current_color == color2 else color2
        button.configure(highlightbackground=new_color)
        button.after(500, pulsate_button, button, color1, color2)

class Menu:
    def __init__(self, root, gui, start_game_callback):
        self.root = root
        self.gui = gui
        self.start_game_callback = start_game_callback

    def display_main_menu(self):
        self.gui.canvas.delete("all")
        self.gui.canvas.config(bg="black", highlightthickness=0)
        self.menu_buttons = []  # used to create a list of the buttons so we can clear them later on

        try:
            self.image = Image.open("pacman_logo.png") 
            self.original_image = self.image.resize((500, 400), Image.LANCZOS)
            self.pacman_logo = ImageTk.PhotoImage(self.original_image)
            self.gui.canvas.create_image(300, 150, image=self.pacman_logo, anchor="center")  
        except Exception as e:
            print(f"Error loading Pac-Man logo: {e}")
            self.gui.canvas.create_text(
                300, 150, text="PAC-MAN", fill="yellow", font=("Courier", 40, "bold")
            )

        start_button = tk.Button(
            self.gui.canvas,
            text="Start Game !",
            font=("Courier", 18, "bold"),
            height=2,
            relief="ridge",  
            bd=0.5,          
            highlightbackground="yellow",  
            highlightcolor="red",          
            highlightthickness=2,
            command=lambda: [self.clear_menu(), self.start_game_callback()]
        )
        self.gui.canvas.create_window(290, 300, window=start_button)
        self.menu_buttons.append(start_button)
        pulsate_button(start_button, "yellow", "sky blue")


        instructions_button = tk.Button(
            self.gui.canvas,
            text="Instructions",
            font=("Courier", 14,"bold"),
            height=2,
            relief="ridge",  
            bd=0.5,            
            highlightbackground="red",  
            highlightcolor="red",       
            highlightthickness=2,
            command=lambda: messagebox.showinfo("Instructions", "Use arrow keys to move.\nAvoid the ghosts and collect all dots and fruits!")
        )
        self.gui.canvas.create_window(290, 350, window=instructions_button)
        self.menu_buttons.append(instructions_button)

        exit_button = tk.Button(
            self.gui.canvas,
            text="Exit",
            font=("Courier", 14,"bold"),
            height=2,
            relief="ridge",  
            bd=0.5,          
            highlightbackground="red",  
            highlightcolor="red",        
            highlightthickness=2,
            command=self.root.quit
        )
        self.gui.canvas.create_window(290, 400, window=exit_button)
        self.menu_buttons.append(exit_button)

    def clear_menu(self):
        self.gui.canvas.delete()  

        for button in self.menu_buttons:  # removes the buttons before the game starts, as it caused bugs
            button.destroy()
        self.menu_buttons.clear()  
    
    
