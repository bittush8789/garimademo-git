import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            b = tk.Button(row_frame, text=btn, font=("Arial", 18),
                          command=calculate)
        else:
            b = tk.Button(row_frame, text=btn, font=("Arial", 18),
                          command=lambda x=btn: click(x))
        b.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 18), command=clear)
clear_btn.pack(fill="both", padx=10, pady=10)

# Run app
root.mainloop()
