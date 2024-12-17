import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

try:
    image = Image.open("pacman.png")
    image = image.resize((40, 40), Image.LANCZOS)
    pacman_image = ImageTk.PhotoImage(image)
    canvas.create_image(100, 100, image=pacman_image)
    print("Image loaded and displayed successfully!")
except Exception as e:
    print(f"Error loading image: {e}")

root.mainloop()
