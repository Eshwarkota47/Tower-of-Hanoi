import tkinter as tk
import time
#from PIL import ImageTk, Image

# Tower of Hanoi algorithm
def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        target.append(source.pop())
        draw_towers()
        root.update()
        time.sleep(0.75)  # Add a delay of 1 second
        hanoi(n - 1, auxiliary, target, source)

# Draw the current state of the towers
def draw_towers():
    canvas.delete("all")
    for i in range(3):
        canvas.create_rectangle(
            175 + i * 200 - 5,
            250,
            175 + i * 200 + 5,~
            50,
            fill="grey",  # Color the rods grey
            outline='black'
        )
        for j in range(len(towers[i])):
            width = base_width + towers[i][j] * width_increment
            canvas.create_rectangle(
                175 + i * 200 - width / 2,
                250 - j * height_increment,
                175 + i * 200 + width / 2,
                250 - (j + 1) * height_increment,
                fill=colors[towers[i][j]-1],  # Color the disks differently
                outline="black"
            )

# Get the number of disks from the user
def get_num_disks():
    global num_disks
    num_disks = int(entry.get())
    root.destroy()

# GUI initialization
root = tk.Tk()
root.title("Tower of Hanoi")
root.resizable(0,0)
root.geometry("800x400")
img = tk.Image.open('C:\\Users\\emera\\Downloads\\hanoi.png')
bg = tk.Image.PhotoImage(img)


#Fonts
custom_font = ("Helvetica", 12, "bold")
font2 = ("Times New Roman", 12)

# Create entry field for the number of disks
label = tk.Label(root, text="Enter the number of disks:",font=("Times New Roman", 14, "bold"))
label.pack(pady=10)
entry = tk.Entry(root,font=("Helvetica", 12))
entry.pack(pady=35)
button = tk.Button(root, text="ENTER", command=get_num_disks, font=font2)
button.pack()

root.mainloop()

# Tower initialization
towers = [list(range(num_disks, 0, -1)), [], []]

# GUI initialization
root = tk.Tk()
root.title("Tower of Hanoi")
root.geometry("800x400")

canvas = tk.Canvas(root, width=800, height=40)
canvas.pack(padx=20)

# Tower parameters
base_width = 80
width_increment = 20
height_increment = 20

# Define colors for the disks
colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink', 'cyan', 'magenta', 'brown']

# Draw initial towers
draw_towers()

# Solve Tower of Hanoi
hanoi(num_disks, towers[0], towers[2], towers[1])

root.mainloop()
