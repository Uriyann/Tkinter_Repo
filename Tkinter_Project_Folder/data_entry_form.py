import tkinter as tk
from tkinter import ttk
from tkinter import *


window = tk.Tk()
window.title("Login Form")
window.geometry('600x600')

# Frame
frame = tk.Frame(window)
frame.pack()

# User Frame
user_info_frame = tk.LabelFrame(frame, text="User Information", font= ("times new roman", 17))
user_info_frame.grid(row=0, column=0, sticky= NSEW, pady=20, padx=20)

# Name Label and Entry
first_name_label = tk.Label(user_info_frame, text= "First Name:", font= ("arial normal", 10))
first_name_entry = tk.Entry(user_info_frame)

middle_name_label = tk.Label(user_info_frame, text= "Middle Name:", font= ("arial normal", 10))
middle_name_entry = tk.Entry(user_info_frame)

last_name_label = tk.Label(user_info_frame, text= "Last Name:", font= ("arial normal", 10))
last_name_entry = tk.Entry(user_info_frame)


# User Info Grid
first_name_label.grid(row=0, column=0, pady=5, sticky= "e")
first_name_entry.grid(row=0, column=1, pady=3, padx=3)

middle_name_label.grid(row=1, column=0, pady=5, sticky= "e")
middle_name_entry.grid(row=1, column=1, pady=3)

last_name_label.grid(row=2, column=0, pady=5, sticky= "e")
last_name_entry.grid(row=2, column=1, pady=3)


# Secondary Frame
second_frame = tk.LabelFrame(frame)
second_frame.grid(row=1, column=0, sticky= NSEW, pady=20, padx=20)

# Age
age_label = tk.Label(second_frame, text= "Age:", font= ("arial normal", 10))
age_entry = tk.Spinbox(second_frame, from_=0, to=100, width=15)

# Birthdate
birthdate_label = tk.Label(second_frame, text= "Birthdate MM/dd/YYYY:", font= ("arial normal", 10))
month_entry = ttk.Combobox(second_frame, values= [
                                                        "January", "February", "March", "April",
                                                        "May", "June", "July", "August",
                                                        "September", "October", "November", "December"
                                                    ], state= "readonly", font= ("arial normal", 10), width=10)
days = list(range(1, 31))
day_entry = ttk.Combobox(second_frame, values= days, state= "readonly", font= ("arial normal", 10), width=5)
years = list(range(2000, 2051))
year_entry = ttk.Combobox(second_frame, values= years, state= "readonly", font= ("arial normal", 10), width=5)

# Gender
gender_label = tk.Label(second_frame, text= "Gender:", font= ("arial normal", 10))
gender = IntVar()
male_entry = tk.Radiobutton(second_frame, text="Male", variable=gender, value="Male")
female_entry = tk.Radiobutton(second_frame, text="Female", variable=gender, value="Female")

# Birthplace
birthplace_label = tk.Label(second_frame, text= "Birthplace:", font= ("arial normal", 10))
birthplace_entry = tk.Entry(second_frame, width=15)


# Secondary Frame Info Grid

# Age Grid
age_label.grid(row=4, column=0, pady=5, padx=5, sticky= "e")
age_entry.grid(row=4, column=1, pady=5, padx=5)

# Birthdate Grid
birthdate_label.grid(row=4, column=2, pady=5, padx=5, sticky= "e")
month_entry.grid(row=4, column=3, pady=5, padx=2)
day_entry.grid(row=4, column=4, pady=5, padx=2)
year_entry.grid(row=4, column=5, pady=5, padx=2)

# Gender Grid
gender_label.grid(row=5, column=0, pady=5, padx=5, sticky= "e")
male_entry.grid(row=5, column=1, pady=5, padx=2)
female_entry.grid(row=6, column=1, pady=5, padx=2)

# Birthplace Grid
birthplace_label.grid(row=5, column=2, pady=5, padx=5, sticky= "e")
birthplace_entry.grid(row=5, column=3, pady=5, padx=2)


# Third Frame
third_frame = tk.LabelFrame(frame)
third_frame.grid(row=2, column=0, sticky= NSEW, pady=20, padx=20)

# Nationality
nationality_label = tk.Label(third_frame, text= "Nationality:", font= ("arial normal", 10))
nationality_entry = ttk.Combobox(third_frame, values= ["Filipino", "Japanese", "American", "Chinese"], state= "readonly", font= ("arial normal", 10), width=15)

# Marital Status
marital_label = tk.Label(third_frame, text= "Marital Status:", font= ("arial normal", 10))
marital_entry = ttk.Combobox(third_frame, values= ["Single", "Married", "Divorced", "Widowed"], state= "readonly", font= ("arial normal", 10), width=10)

# Religion
religion_label = tk.Label(third_frame, text= "Religion:", font= ("arial normal", 10))
religion_entry = ttk.Combobox(third_frame, values= ["Roman Catholic", "Iglesia", "Muslim"], state= "readonly", font= ("arial normal", 10), width=15)


# Third Frame Info Grid

# Nationality Grid
nationality_label.grid(row=8, column=0, pady=5, padx=5, sticky= "e")
nationality_entry.grid(row=8, column=1, pady=5, padx=2)

# Marital Status Grid
marital_label.grid(row=8, column=2, pady=5, padx=5, sticky= "e")
marital_entry.grid(row=8, column=3, pady=3, padx=3)

# Religion Grid
religion_label.grid(row=9, column=0, pady=5, padx=5, sticky= "e")
religion_entry.grid(row=9, column=1, pady=5, padx=2)





window.mainloop()