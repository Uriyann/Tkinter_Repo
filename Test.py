import tkinter as tk

def handle_enter(event):
    print("Enter key pressed!")
    # Add your desired functionality here

window = tk.Tk()
entry = tk.Entry(window)
entry.bind('<Return>', handle_enter) # Bind Enter key press to handle_enter function
entry.pack()
window.mainloop()