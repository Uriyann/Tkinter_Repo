import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root, bg="white")
frame.pack(pady=50)

# Entry Widgets
user_entry = tk.Entry(frame, font=("Arial", 19), bg="white", fg="black")
pass_entry = tk.Entry(frame, font=("Arial", 19), bg="white", fg="black")
user_entry.pack(pady=10)
pass_entry.pack(pady=10)

# Overlay Labels
user_label = tk.Label(frame, text="Username", font=("Arial", 15), bg="white", fg="gray58")
user_label.place(in_=user_entry, x=5, y=1)  # Adjust x and y as needed

pass_label = tk.Label(frame, text="Password", font=("Arial", 15), bg="white", fg="gray58")
pass_label.place(in_=pass_entry, x=5, y=1)  # Adjust x and y as needed

root.mainloop()
