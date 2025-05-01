from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Score Tracker")
window.geometry("500x600")

main_frame = Frame(window).place(relx=0.5, rely=0.5, anchor= CENTER)

name_label = Label(main_frame, text= "Name:").grid(row=0, column=1)


window.mainloop()