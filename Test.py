import tkinter as tk

root = tk.Tk()
root.title("Log In")
root.configure(bg="white")

# Configure grid layout
root.columnconfigure(0, weight=1)

# Title Label
title = tk.Label(root, text="Log In", font=("Times New Roman", 24, "bold"), bg="white")
title.grid(row=0, column=0, pady=(30, 20))

# Form Frame
form_frame = tk.Frame(root, bg="white")
form_frame.grid(row=1, column=0, padx=50, sticky="ew")

# Username Label
username_label = tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="white")
username_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

# Entry without border
username_entry = tk.Entry(form_frame, bd=0, font=("Arial", 12))
username_entry.grid(row=1, column=0, sticky="ew")

# Underline (Frame with black background)
underline = tk.Frame(form_frame, height=2, bg="black")
underline.grid(row=2, column=0, sticky="ew", pady=(0, 15))

# Placeholder logic (optional)
def clear_placeholder(event):
    if username_entry.get() == "Username:":
        username_entry.delete(0, tk.END)

def add_placeholder(event):
    if not username_entry.get():
        username_entry.insert(0, "Username:")

username_entry.insert(0, "Username:")
username_entry.bind("<FocusIn>", clear_placeholder)
username_entry.bind("<FocusOut>", add_placeholder)

root.mainloop()
