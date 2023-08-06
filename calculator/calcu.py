import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display and input expressions
entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operators
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font="Arial 20", padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

# Start the main event loop
root.mainloop()
