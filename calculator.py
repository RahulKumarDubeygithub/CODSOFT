import tkinter as tk
# Define the function to handle button clicks
def on_click(event):
    # Get the text of the clicked button
    text = event.widget.cget("text")
    # If the "=" button is clicked, try to evaluate the expression in the entry field
    if text == "=":
        try:
            # Evaluate the expression using the 'eval' function
            result = eval(entry.get())  # Using eval to perform arithmetic evaluation
            # Clear the entry field and insert the result
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            # If there's an error in the expression, clear the entry field and show "Error"
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    # If the "C" button is clicked, clear the entry field
    elif text == "C":
        entry.delete(0, tk.END)
    # If the "←" button is clicked, remove the last character from the entry field
    elif text == "←":
        entry.delete(len(entry.get()) - 1)
    # For other buttons (numbers, operators, etc.), add their text to the entry field
    else:
        entry.insert(tk.END, text)

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Set the initial size and prevent resizing of the window
root.geometry("377x395")  # Set the initial size of the window to width=377, height=395
root.minsize(90, 194)    # Set the minimum size the window can be resized to
root.maxsize(700, 750)    # Set the maximum size the window can be resized to

# Create an input field (Entry widget) for displaying and inputting numbers and expressions
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # Apply sticky="nsew"
"""nsew is a combination of the four cardinal directions: north, south, east, and west. It stands for "north-south-east-west," meaning the widget will stick (expand) to all sides of its cell.
Here's what each direction means:
n: Sticks to the top (north) side of the cell.
s: Sticks to the bottom (south) side of the cell.
e: Sticks to the right (east) side of the cell.
w: Sticks to the left (west) side of the cell.
By setting sticky="nsew", the buttons will expand to fill the available space within their respective cells as the window is resized. This ensures that the buttons are evenly spaced and maintain their size and position relative to the grid cells."""

# Define the buttons' text in a list
buttons = [
    "C", "√", "/", "←",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "!", "0", ".", "=",
]

# Add buttons to the window using a loop
r = 1
c = 0
for button_text in buttons:
    btn = tk.Button(root, text=button_text, font=("Arial", 15), padx=10, pady=10, width=5, height=2)
    # Use grid layout to place buttons in their respective rows and columns
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
    c += 1
    if c > 3:
        c = 0
        r += 1

# Configure rows and columns to resize properly when the window is resized
# Setting 'weight' to 1 means the rows and columns will expand proportionally when the window is resized
for i in range(1, 6):  # Assuming there are 5 rows (0 for the entry field and 4 for buttons)
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # Assuming there are 4 columns for buttons
    root.grid_columnconfigure(i, weight=1)

# Bind the buttons to the on_click function
# For each button in the application, bind the left mouse click event to the on_click function
for btn in root.winfo_children():
    btn.bind("<Button-1>", on_click)
    """In this line, we are iterating through all the children of the root window using root.winfo_children(). This method returns a list of all the widgets (buttons, entry field, etc.) that are direct children of the root window.

        The "bind" method is used to associate an event with a function. Here, we are binding the left mouse button click event to the on_click function for all the buttons in the application.

        "<Button-1>" is the event string for the left mouse button click event. In Tkinter, mouse events are represented using event strings. Here are some common event strings for mouse-related events:
        <Button-1>: Left mouse button click
        <Button-2>: Middle mouse button click
        <Button-3>: Right mouse button click
        <Double-Button-1>: Left mouse button double-click"""

# Run the main event loop
# Start the main event loop to display the window and handle user interactions
root.mainloop()