import tkinter as tk

# Function to update the entry field
def click(event):
    current_text = entry.get()
    clicked_button = event.widget.cget("text")
    if clicked_button == "=":
        try:
            result = eval(current_text)  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif clicked_button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, clicked_button)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, width=16, font=("Arial", 24), bd=8, insertwidth=4, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)  # 'C' button spans 4 columns
]

# Create and place the buttons
for (text, row, column, *span) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18))
    button.grid(row=row, column=column, columnspan=span[0] if span else 1)
    button.bind('<Button-1>', click)

# Run the application
root.mainloop()