import tkinter as tk
import math


def on_button_click(event):
    button_text = event.widget.cget("text")
    current_text = entry.get()

    if button_text == "AC":
        entry.delete(0, tk.END)

    elif button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as ex:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "2√ ":
        try:
            result = math.sqrt(float(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as ex:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "∛x":
        calculate_thirdroot()

    elif button_text == "DEL":
        current_text = entry.get()
        updated_text = current_text[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, updated_text)
    elif button_text == "x²":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(float(current_text) ** 2))

    elif button_text == "log":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.log10(float(current_text))))

    elif button_text == "1/x":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(1 / float(current_text)))

    elif button_text == "x³":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(float(current_text) ** 3))
    
    elif button_text == "%":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(float(current_text) / 100))

    elif button_text == "div":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(float(current_text) // 2 ))

    elif button_text == "Exp":
        entry.insert(tk.END, "**")
    
    elif button_text == "x^n":       
        calculate_xpown()
    
    elif button_text == "e^":       
         calculate_e1()

    elif button_text == "e":
        calculate_e()

    elif button_text == "π":
        calculate_pi()
                     
    elif button_text == "sin":
        calculate_sin()

    elif button_text == "cos":
        calculate_cos()

    elif button_text == "tan":
        calculate_tan()

    elif button_text == "cot":
        calculate_cot()

    elif button_text == "abs":
        calculate_abs()
    
    elif button_text == "x!":
        calculate_fact()

    elif button_text == "10^x":
        calculate_10power()
    
    else:
        entry.insert(tk.END, button_text)

#defining functions 

def calculate_thirdroot():
    current_text = entry.get()
    try:
        value = int(current_text)
        result = value**(1/3)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_xpown():
    try:
        dialog = tk.Toplevel(root)  # Create a new dialog window
        dialog.title("Enter Base and Power")
        
        tk.Label(dialog, text="Base:").grid(row=0, column=0)
        base_entry = tk.Entry(dialog)
        base_entry.grid(row=0, column=1)
        
        tk.Label(dialog, text="Power:").grid(row=1, column=0)
        power_entry = tk.Entry(dialog)
        power_entry.grid(row=1, column=1)
        
        confirm_button = tk.Button(dialog, text="Calculate", command=lambda: calculate_power_result(dialog, base_entry.get(), power_entry.get()))
        confirm_button.grid(row=2, columnspan=2)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_power_result(dialog, base_value, power_value):
    try:
        base_value = float(base_value)
        power_value = float(power_value)
        result = base_value ** power_value
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        dialog.destroy()  # Close the custom dialog
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_e1():
    current_text = entry.get()
    try:
        value = float(current_text)
        result = math.exp(value)  # Use math.exp() for e raised to the power of a value
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_e():
    current_text = entry.get()
    try:
        e = math.exp(1)
        value = float(current_text)
        result = e * value  # Use math.exp() for e raised to the power of a value
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_pi():
    current_text = entry.get()
    try:
        value = float(current_text)
        result = value * math.pi  # Use math.pi directly as a constant
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_sin():
    current_text = entry.get()
    try:
        angle_in_degrees = float(current_text)
        angle_in_radians = math.radians(angle_in_degrees)
        result = math.sin(angle_in_radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_cos():
    current_text = entry.get()
    try:
        angle_in_degrees = float(current_text)
        angle_in_radians = math.radians(angle_in_degrees)
        result = math.cos(angle_in_radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_tan():
    current_text = entry.get()
    try:
        angle_in_degrees = float(current_text)
        angle_in_radians = math.radians(angle_in_degrees)
        result = math.tan(angle_in_radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_cot():
    current_text = entry.get()
    try:
        angle_in_degrees = float(current_text)
        angle_in_radians = math.radians(angle_in_degrees)
        result = 1 / math.tan(angle_in_radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 

def calculate_abs():
    current_text = entry.get()
    try:
        value = float(current_text)
        result=abs(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 

def calculate_fact():
    current_text = entry.get()
    try:
        value = int(current_text)  # Factorial is typically calculated for integers
        result = fact(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1) 

def calculate_10power():
    current_text = entry.get()
    try:
        current_value = float(current_text)
        result = 10 ** current_value
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()   
root.title("Scientific Calculator")
root.geometry() 

root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"+{x_coordinate}+{y_coordinate}")

entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=5, sticky="ew")

buttons = [
    ("abs", 1, 0), ("div", 1, 1), ("x!", 1, 2), ("e", 1, 3), ("e^", 1, 4),
    ("sin", 2, 0),("cos", 2, 1),("tan", 2, 2),("cot", 2, 3),("π", 2, 4),
    ("x²", 3, 0),("x³", 3, 1),("x^n",3,2),("1/x",3,3),("10^x",3,4),
    ("2√ ", 4, 0),("∛x", 4, 1),("log", 4, 2),("AC", 4, 3),("DEL", 4, 4),
    ("7", 5, 0), ("8", 5, 1), ("9", 5, 2),("*", 5, 3),("/", 5, 4),
    ("4", 6, 0), ("5", 6, 1), ("6", 6, 2),("+", 6, 3),("-", 6, 4),
    ("1", 7, 0), ("2", 7, 1), ("3", 7, 2), ("(", 7, 3),(")", 7, 4),
    ("0", 8, 0), (".", 8, 1),("Exp", 8, 2),("=", 8, 3),("%", 8, 4)

]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font="Arial 15", padx=13, pady=13, bg="blue")
    if text in buttons:
        button.config(bg="lightblue")   
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

root.mainloop()