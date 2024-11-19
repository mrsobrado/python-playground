import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Constellation Creator")
root.geometry("800x600")

# Canvas for star placement and constellation creation
canvas = tk.Canvas(root, bg="black", width=800, height=600)
canvas.pack()

# List to store the coordinates of stars
stars = []

# Function to place stars
def place_star(event):
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="white")  # Draw star
    stars.append((x, y))  # Add star coordinates to list

# Function to draw lines between stars
def draw_constellation():
    canvas.delete("line")  # Clear previous lines
    for i in range(len(stars)-1):
        x1, y1 = stars[i]
        x2, y2 = stars[i+1]
        canvas.create_line(x1, y1, x2, y2, fill="white", tags="line")

# Function to clear the canvas
def clear_canvas():
    global stars
    stars = []  # Clear stars list
    canvas.delete("all")  # Delete all items from canvas

# Bind mouse click to place stars
canvas.bind("<Button-1>", place_star)

# Button to draw constellation
draw_button = tk.Button(root, text="Draw Constellation", command=draw_constellation)
draw_button.pack()

# Button to clear the canvas
clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

# Run the Tkinter event loop
root.mainloop()
