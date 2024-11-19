import tkinter as tk
import pygame
import random

# Initialize Pygame for sound
pygame.init()

# Create the main application window
root = tk.Tk()
root.title("Starmelody Maker")
root.geometry("800x600")

# Canvas for placing stars
canvas = tk.Canvas(root, bg="black", width=800, height=600)
canvas.pack()

# Generate a random sound frequency
def play_sound():
    freq = random.randint(200, 1000)  # Random frequency in Hz
    duration = 200  # Sound duration in ms
    pygame.mixer.Sound(frequency=freq).play()

# Place stars on click
def place_star(event):
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="white")
    play_sound()

# Bind click event to the canvas
canvas.bind("<Button-1>", place_star)

# Run the Tkinter event loop
root.mainloop()

# Quit Pygame when done
pygame.quit()
