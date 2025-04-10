import tkinter as tk

window = tk.Tk()
window.title("Calc")
window.geometry('400x400')

# frame = tk.Frame()

num_entry = tk.Entry(window)
ans_entry = tk.Entry(window)

seven = tk.Button(window, text="7", font=("Arial", 15))
eight = tk.Button(window, text="8", font=("Arial", 15))
nine = tk.Button(window, text="9", font=("Arial", 15))
div = tk.Button(window, text="/", font=("Arial", 15))

four = tk.Button(window, text="4", font=("Arial", 15))
five = tk.Button(window, text="5", font=("Arial", 15))
six = tk.Button(window, text="6", font=("Arial", 15))
mult = tk.Button(window, text="*", font=("Arial", 15))

one = tk.Button(window, text="1", font=("Arial", 15))
two = tk.Button(window, text="2", font=("Arial", 15))
three = tk.Button(window, text="3", font=("Arial", 15))
min = tk.Button(window, text="-", font=("Arial", 15))

clear = tk.Button(window, text="C", font=("Arial", 15))
zero = tk.Button(window, text="0", font=("Arial", 15))
equal = tk.Button(window, text="=", font=("Arial", 15))
add = tk.Button(window, text="+", font=("Arial", 15))


num_entry.grid(row=0, column=0, columnspan=1, pady= 4)
ans_entry.grid(row=1, column=0, columnspan=1, pady= 4)

seven.grid(row=2, column= 0, rowspan=1, pady= 5)
eight.grid(row=2, column= 1, rowspan=1, pady= 5)
nine.grid(row=2, column= 2, rowspan=1, pady= 5)
div.grid(row=2, column= 3, rowspan=1, pady= 5)

four.grid(row=3, column= 0, rowspan=1, pady= 5)
five.grid(row=3, column= 1, rowspan=1, pady= 5)
six.grid(row=3, column= 2, rowspan=1, pady= 5)
mult.grid(row=3, column= 3, rowspan=1, pady= 5)

one.grid(row=4, column= 0, rowspan=1, pady= 5)
two.grid(row=4, column= 1, rowspan=1, pady= 5)
three.grid(row=4, column= 2, rowspan=1, pady= 5)
min.grid(row=4, column= 3, rowspan=1, pady= 5)

clear.grid(row=5, column= 0, rowspan=1, pady= 5)
zero.grid(row=5, column= 1, rowspan=1, pady= 5)
equal.grid(row=5, column= 2, rowspan=1, pady= 5)
add.grid(row=5, column= 3, rowspan=1, pady= 5)

# frame.pack()


window.mainloop()