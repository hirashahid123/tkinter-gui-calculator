import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Input field
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Function to add text
def click(value):
    entry.insert(tk.END, value)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear input
def clear():
    entry.delete(0, tk.END)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True ,fill="both")

    for button in row:

        if button == "=":
            action = calculate
        else:
            action = lambda x=button: click(x)

        btn=tk.Button(
            frame,
            text=button,
            width=5,
            height=2,
            font=("Arial", 16),
            command=action
        )
        btn.pack(side=tk.LEFT, padx=5, pady=5)

# Clear button
tk.Button(
    root,
    text="Clear",
    width=22,
    height=2,
    font=("Arial", 14),
    command=clear
).pack(pady=10)

# Run app
root.mainloop()
