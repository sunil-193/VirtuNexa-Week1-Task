import tkinter as tk
from tkinter import messagebox
import logging

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def log_operation(operation, x, y, result):
    logging.info(f"{operation}: {x} and {y} = {result}")

def calculate(operation):
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        
        if operation == 'add':
            result = add(x, y)
        elif operation == 'subtract':
            result = subtract(x, y)
        elif operation == 'multiply':
            result = multiply(x, y)
        elif operation == 'divide':
            result = divide(x, y)
        else:
            raise ValueError("Invalid operation.")

        result_label.config(text=f"Result: {result}")
        log_operation(operation, x, y, result)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Create buttons for operations
tk.Button(root, text="Add", command=lambda: calculate('add')).pack()
tk.Button(root, text="Subtract", command=lambda: calculate('subtract')).pack()
tk.Button(root, text="Multiply", command=lambda: calculate('multiply')).pack()
tk.Button(root, text="Divide", command=lambda: calculate('divide')).pack()

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
