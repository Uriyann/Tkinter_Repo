import tkinter as tk

window = tk.Tk()
window.title("Calc")
window.geometry('400x400')

frame = tk.Frame()

num_entry = tk.Entry(frame)
ans_entry = tk.Entry(frame)

num_entry.grid(row=0, column=0, rowspan=1, pady= 4)
ans_entry.grid(row=1, column=0, rowspan=1, pady= 4)

frame.pack()


window.mainloop()