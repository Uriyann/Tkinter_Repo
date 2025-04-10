import tkinter as tk

window = tk.Tk()
window.title("Calc")
window.geometry('350x425')

# Frames
entry_frame = tk.Frame()
num_frame = tk.Frame()

# Entries
num_entry = tk.Entry(entry_frame, width= 10, font=("Arial", 15), justify= "right")
ans_entry = tk.Entry(entry_frame, width= 13, font=("Arial", 30), justify= "right")

# First Row
seven = tk.Button(num_frame, text=" 7 ", font=("Arial", 15), width= 5, height= 2)
eight = tk.Button(num_frame, text=" 8 ", font=("Arial", 15), width= 5, height= 2)
nine = tk.Button(num_frame, text=" 9 ", font=("Arial", 15), width= 5, height= 2)
div = tk.Button(num_frame, text=" / ", font=("Arial", 15), width= 5, height= 2)

# Second Row
four = tk.Button(num_frame, text=" 4 ", font=("Arial", 15), width= 5, height= 2)
five = tk.Button(num_frame, text=" 5 ", font=("Arial", 15), width= 5, height= 2)
six = tk.Button(num_frame, text=" 6 ", font=("Arial", 15), width= 5, height= 2)
mult = tk.Button(num_frame, text=" * ", font=("Arial", 15), width= 5, height= 2)

# Third Row
one = tk.Button(num_frame, text=" 1 ", font=("Arial", 15), width= 5, height= 2)
two = tk.Button(num_frame, text=" 2 ", font=("Arial", 15), width= 5, height= 2)
three = tk.Button(num_frame, text=" 3 ", font=("Arial", 15), width= 5, height= 2)
min = tk.Button(num_frame, text=" - ", font=("Arial", 15), width= 5, height= 2)

# Fourth Row
clear = tk.Button(num_frame, text=" C ", font=("Arial", 15), width= 5, height= 2)
zero = tk.Button(num_frame, text=" 0 ", font=("Arial", 15), width= 5, height= 2)
equal = tk.Button(num_frame, text=" = ", font=("Arial", 15), width= 5, height= 2)
add = tk.Button(num_frame, text=" + ", font=("Arial", 15), width= 5, height= 2)


# Grid
num_entry.grid(row=0, column=0, pady= 3, padx= 3, sticky= "news")
ans_entry.grid(row=1, column=0, pady= 3, padx= 3, sticky= "news")

seven.grid(row=2, column= 0, padx= 5, pady= 5)
eight.grid(row=2, column= 1, padx= 5, pady= 5)
nine.grid(row=2, column= 2, padx= 5, pady= 5)
div.grid(row=2, column= 3, padx= 5, pady= 5)

four.grid(row=3, column= 0, padx= 5, pady= 5)
five.grid(row=3, column= 1, padx= 5, pady= 5)
six.grid(row=3, column= 2, padx= 5, pady= 5)
mult.grid(row=3, column= 3, padx= 5, pady= 5)

one.grid(row=4, column= 0, padx= 5, pady= 5)
two.grid(row=4, column= 1, padx= 5, pady= 5)
three.grid(row=4, column= 2, padx= 5, pady= 5)
min.grid(row=4, column= 3, padx= 5, pady= 5)

clear.grid(row=5, column= 0, padx= 5, pady= 5)
zero.grid(row=5, column= 1, padx= 5, pady= 5)
equal.grid(row=5, column= 2, padx= 5, pady= 5)
add.grid(row=5, column= 3, padx= 5, pady= 5)

entry_frame.pack(expand=True)
num_frame.pack(expand=True)

window.mainloop()