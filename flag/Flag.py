import tkinter as tk
import math

root = tk.Tk()
root.title("")
canvas = tk.Canvas(root, width=600, height=450)  
canvas.pack()

box_color = "orange"
border_color = "#2980b9"
box_coords = (50, 50, 550, 150)
box1 = canvas.create_rectangle(box_coords, fill=box_color, outline=border_color)

white_box_coords = (50, 150, 550, 250)  
white_box = canvas.create_rectangle(white_box_coords, fill="white", outline="black")

box2_coords = (50, 250, 550, 350)  
box2 = canvas.create_rectangle(box2_coords, fill="green", outline="black")

center_x = (white_box_coords[0] + white_box_coords[2]) / 2
center_y = (white_box_coords[1] + white_box_coords[3]) / 2

wheel_radius = 30
spoke_length = wheel_radius - 5  
wheel_color = "gray"
wheel_border_color = "black"

canvas.create_oval(center_x - wheel_radius, center_y - wheel_radius,
                   center_x + wheel_radius, center_y + wheel_radius,
                   outline=wheel_border_color, width=2, fill=wheel_color)

for angle in range(0, 360, 15):
    angle_rad = math.radians(angle)
    x1 = center_x + wheel_radius * math.cos(angle_rad)
    y1 = center_y - wheel_radius * math.sin(angle_rad)
    x2 = center_x + spoke_length * math.cos(angle_rad)
    y2 = center_y - spoke_length * math.sin(angle_rad)
    canvas.create_line(center_x, center_y, x2, y2, fill=wheel_border_color)

line_x = box2_coords[0]  
line_y1 = box2_coords[1] - 200 
line_y2 = box2_coords[3] + 200  
canvas.create_line(line_x, line_y1, line_x, line_y2, fill="black", width=3)  
bold_line_width = 1  
canvas.create_line(box2_coords[2], box2_coords[1], box2_coords[2], box2_coords[3], fill="black", width=bold_line_width)

title_label = tk.Label(root, text="Jai", font=("Arial", 30, "bold"), fg="red")
title_label.place(x=250, y=10)  

subtitle_label = tk.Label(root, text="Hind", font=("Arial", 30, "bold"), fg="green")
subtitle_label.place(x=300, y=10)
# Start the Tkinter event loop
root.mainloop()