import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Input Table")

# Define the headers
headers = ["Source", "Measure", "Load"]

# Define the labels and their corresponding widgets
data = [
    ("Vset", "Vin", "Iset"),
    ("Iset", "Iin", "ON", True),
    ("ON", "Vout", "OFF", False),
    ("OFF", "Iout", ""),
]

# Create the headers
for i, header in enumerate(headers):
    tk.Label(root, text=header, borderwidth=2, relief="groove", width=20).grid(row=0, column=i, columnspan=i+2)

# Function to toggle button state and color
def toggle_button(button):
    current_state = button.cget("text")
    if current_state == "ON":
        button.config(text="OFF", bg="white")
    elif current_state == "OFF":
        button.config(text="ON", bg="yellow")
    
# Create the table contents
for row, (source, measure, load, *button) in enumerate(data, start=1):
    # Create source label and entry/button
    tk.Label(root, text=f"{source}:", borderwidth=2, relief="groove", width=20).grid(row=row, column=0)
    if source in ["ON", "OFF", "Enable", "Disable"]:
        btn = tk.Button(root, text=source, width=10, command=lambda: toggle_button(btn))
        if source in ["ON", "Enable"]:
            btn.config(bg="white")
        elif source in ["OFF", "Disable"]:
            btn.config(bg="white")
        btn.grid(row=row, column=1)
    else:
        tk.Entry(root, width=20).grid(row=row, column=1)
    
    # Create measure label and entry
    tk.Label(root, text=f"{measure}:", borderwidth=2, relief="groove", width=20).grid(row=row, column=2)
    tk.Entry(root, width=20).grid(row=row, column=3)
    
    # Create load label and entry/button
    tk.Label(root, text=f"{load}:", borderwidth=2, relief="groove", width=20).grid(row=row, column=4)
    if button:
        if button[0]:
            tk.Button(root, text="ON", width=10, command=lambda: toggle_button(btn)).grid(row=row, column=5)
        else:
            tk.Button(root, text="OFF", width=10, command=lambda: toggle_button(btn)).grid(row=row, column=5)
    else:
        if load:
            tk.Entry(root, width=20).grid(row=row, column=5)

# Run the GUI event loop
root.mainloop()
