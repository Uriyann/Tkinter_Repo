import tkinter as tk
from tkinter import ttk
from tkinter import *


window = tk.Tk()
window.title("Data Entry Form")
window.geometry('800x800')

def data_enter():
    
    # User Name Info
    first_name = first_name_entry.get()
    middle_name = middle_name_entry.get()
    last_name = last_name_entry.get()

    # 2nd Info
    age = age_entry.get()
    birth_month = month_entry.get()
    birth_day = day_entry.get()
    birth_year = year_entry.get()

    birth_place = birthplace_entry.get()

    # 3rd Info
    nationality = nationality_entry.get()
    marital = marital_entry.get()
    religion = religion_entry.get()
    language = language_entry.get()

    # 4th Info
    street = street_entry.get()
    street_num = street_num_entry.get()
    brgy = brgy_entry.get()
    zip_code = zip_code_entry.get()
    city = city_entry.get()
    province = province_entry.get()

    # 5th Info
    email = email_entry.get()
    phone_num = phone_num_entry.get()

    print("Data Entry Form:\n\n" \
          "First Name:",first_name,
          "\nMiddle Name:",middle_name,
          "\nLast Name:",last_name,
          
          "\n\nAge:",age,
          f"\nBirth Date: {birth_month}, {birth_day}, {birth_year}"
          "\nBirth Place:",birth_place,
          
          "\n\nNationality:",nationality,
          "\nMarital Status:",marital,
          "\nReligion:",religion,
          "\nLanguage:",language,
          
          f"\n\nStreet/No.: {street}, {street_num}"
          "\nBarangay:",brgy,
          f"\nZip Code/City: {zip_code}, {city}"
          "\nProvince:",province,
          
          "\n\nEmail:",email,
          "\nPhone Number:",phone_num)


# Frame
frame = tk.Frame(window)
frame.pack()

# User Frame
user_info_frame = tk.LabelFrame(frame, text="User Information", font= ("times new roman", 15))
user_info_frame.grid(row=0, column=0, sticky= NSEW, pady=10, padx=20)

# Name Label and Entry
first_name_label = tk.Label(user_info_frame, text= "First Name:", font= ("arial normal", 10))
first_name_entry = tk.Entry(user_info_frame)

middle_name_label = tk.Label(user_info_frame, text= "Middle Name:", font= ("arial normal", 10))
middle_name_entry = tk.Entry(user_info_frame)

last_name_label = tk.Label(user_info_frame, text= "Last Name:", font= ("arial normal", 10))
last_name_entry = tk.Entry(user_info_frame)

# Image
image_file = tk.PhotoImage(file = r'C:\Users\M S I\Desktop\Tkinter_Repository\Tkinter_Project_Folder\wallhaven-m38z5y.png')
image = image_file.subsample(6, 6)

Label(user_info_frame, image = image).grid(row =0, column =5,
       columnspan = 3, rowspan = 3, padx = 111, pady = 10)

# User Info Grid
first_name_label.grid(row=0, column=0, pady=5, sticky= "e")
first_name_entry.grid(row=0, column=1, pady=3, padx=3)

middle_name_label.grid(row=1, column=0, pady=5, sticky= "e")
middle_name_entry.grid(row=1, column=1, pady=3)

last_name_label.grid(row=2, column=0, pady=5, sticky= "e")
last_name_entry.grid(row=2, column=1, pady=3)


# Secondary Frame
second_frame = tk.LabelFrame(frame)
second_frame.grid(row=1, column=0, sticky= NSEW, pady=5, padx=20)

# Age
age_label = tk.Label(second_frame, text= "Age:", font= ("arial normal", 10))
age_entry = tk.Spinbox(second_frame, from_=0, to=100, width=15)

# Birthdate
birthdate_label = tk.Label(second_frame, text= "Birthdate:", font= ("arial normal", 10))
month_entry = ttk.Combobox(second_frame, values= ["January", "February", "March", "April",
                                                  "May", "June", "July", "August",
                                                  "September", "October", "November", "December"], 
                                                  state= "readonly", font= ("arial normal", 10), width=10)
days = list(range(1, 32))
day_entry = ttk.Combobox(second_frame, values= days, state= "readonly", font= ("arial normal", 10), width=5)
years = list(range(1950, 2051))
year_entry = ttk.Combobox(second_frame, values= years, state= "readonly", font= ("arial normal", 10), width=5)

# Gender
gender_label = tk.Label(second_frame, text= "Gender:", font= ("arial normal", 10))
gender = tk.IntVar()
male_entry = tk.Radiobutton(second_frame, text="Male", variable=gender, value="Male")
female_entry = tk.Radiobutton(second_frame, text="Female", variable=gender, value="Female")

# Birthplace
birthplace_label = tk.Label(second_frame, text= "Birthplace:", font= ("arial normal", 10))
birthplace_entry = tk.Entry(second_frame, width=15)


# Secondary Frame Info Grid

# Age Grid
age_label.grid(row=0, column=0, pady=5, padx=5, sticky= "e")
age_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(second_frame, text="").grid(row=0, column=2, padx=21)

# Birthdate Grid
birthdate_label.grid(row=0, column=3, pady=5, padx=5, sticky= "e")
month_entry.grid(row=0, column=4, pady=5, padx=2)
month_entry.set("MM")
day_entry.grid(row=0, column=5, pady=5, padx=2)
day_entry.set("dd")
year_entry.grid(row=0, column=6, pady=5, padx=2)
year_entry.set("YYYY")

# Gender Grid
gender_label.grid(row=1, column=0, pady=5, padx=5, sticky= "e")
male_entry.grid(row=1, column=1, sticky="w")
female_entry.grid(row=1, column=1, sticky="e")

# Birthplace Grid
birthplace_label.grid(row=1, column=3, pady=5, padx=5, sticky= "e")
birthplace_entry.grid(row=1, column=4, pady=5, padx=2)


# Third Frame
third_frame = tk.LabelFrame(frame)
third_frame.grid(row=2, column=0, sticky= NSEW, pady=5, padx=20)

# Nationality
nationality_label = tk.Label(third_frame, text= "Nationality:", font= ("arial normal", 10))
nationality_entry = ttk.Combobox(third_frame, values= ["Filipino", "American", "British", "Chinese", "Indian", "Japanese", "Korean", 
                                                       "German", "French", "Italian", "Canadian", "Australian", "Spanish", "Mexican",
                                                       "Brazilian", "Russian", "Indonesian", "Vietnamese", "Thai", "Saudi Arabian",
                                                       "South African", "Malaysian", "Singaporean", "Other"], 
                                                       state= "readonly", font= ("arial normal", 10))

# Marital Status
marital_label = tk.Label(third_frame, text= "Marital Status:", font= ("arial normal", 10))
marital_entry = ttk.Combobox(third_frame, values= ["Single", "Married", "Divorced", "Widowed"], state= "readonly", font= ("arial normal", 10))

# Religion
religion_label = tk.Label(third_frame, text= "Religion:", font= ("arial normal", 10))
religion_entry = ttk.Combobox(third_frame, values= ["Roman Catholic", "Iglesia ni Cristo", "Evangelical Christianity", "Aglipayan (Philippine Independent Church)",
                                                    "Islam", "Seventh-day Adventist", "Baptist", "Jehovah's Witnesses", "Born Again Christianity",
                                                    "Methodist", "Orthodox Christianity", "Church of Christ (Disciples)", "Buddhism",
                                                    "Hinduism", "Other"], 
                                                    state= "readonly", font= ("arial normal", 10))

language_label = tk.Label(third_frame, text= "Language:", font= ("arial normal", 10))
language_entry = ttk.Combobox(third_frame, values= ["English", "Filipino", "Mandarin Chinese", "Spanish", "Hindi", "Arabic",
                                                    "Bengali", "Portuguese", "Russian", "Japanese", "French", "German", "Korean",
                                                    "Italian", "Vietnamese", "Turkish", "Persian (Farsi)", "Swahili", "Thai", "Malay/Indonesian"], 
                                                    state= "readonly", font= ("arial normal", 10))

# Third Frame Info Grid

# Nationality Grid
nationality_label.grid(row=0, column=0, pady=5, padx=5, sticky= "e")
nationality_entry.grid(row=0, column=1, pady=5, padx=2)
nationality_entry.set("Select Nationality")

# Marital Status Grid
marital_label.grid(row=0, column=2, pady=5, padx=5, sticky= "e")
marital_entry.grid(row=0, column=3, pady=3, padx=3)
marital_entry.set("Select Marital Status")

# Religion Grid
religion_label.grid(row=1, column=0, pady=5, padx=5, sticky= "e")
religion_entry.grid(row=1, column=1, pady=5, padx=2)
religion_entry.set("Select Religion")

# Language Grid
language_label.grid(row=1, column=2, pady=5, padx=5, sticky= "e")
language_entry.grid(row=1, column=3, pady=5, padx=2)
language_entry.set("Select Language")

# Fourth Frame
fourth_frame = tk.LabelFrame(frame)
fourth_frame.grid(row=3, column=0, sticky= NSEW, pady=5, padx=20)

# Street/No
street_label = tk.Label(fourth_frame, text= "Street/No:", font= ("arial normal", 10))
street_entry = tk.Entry(fourth_frame, width= 21)
street_num_entry = tk.Entry(fourth_frame, width= 9)

# Barangay
brgy_label = tk.Label(fourth_frame, text= "Barangay:", font= ("arial normal", 10))
brgy_entry = tk.Entry(fourth_frame, width= 23)

# Zip Code/City
zip_code_city_label = tk.Label(fourth_frame, text= "ZIP Code/City:", font= ("arial normal", 10))
zip_code_entry = tk.Entry(fourth_frame, width= 9)
city_entry = tk.Entry(fourth_frame, width= 21)

# Province
province_label = tk.Label(fourth_frame, text= "Country:", font= ("arial normal", 10))
province_entry = ttk.Combobox(fourth_frame, values= [# Luzon
                                                    "Ilocos Norte", "Ilocos Sur", "La Union", "Pangasinan", "Nueva Ecija", "Pampanga",
                                                    "Bulacan", "Rizal", "Laguna", "Batangas", "Quezon", "Palawan",
       
                                                    # Visayas
                                                    "Cebu", "Bohol", "Negros Occidental", "Negros Oriental", "Leyte", "Samar", "Aklan",
                                                    "Capiz", "Iloilo",
       
                                                    # Mindanao
                                                    "Davao del Sur", "Davao del Norte", "Bukidnon", "Misamis Oriental", "Zamboanga del Sur",
                                                    "Lanao del Norte", "South Cotabato", "Maguindanao"], 
                                                    state= "readonly", font= ("arial normal", 10), width= 17)

# Fourth Frame Info Grid

# Street Grid
street_label.grid(row=0, column=0, pady=5, padx=5, sticky= "e")
street_entry.grid(row=0, column=1, columnspan=2, pady=5, padx=2, sticky= "w")
street_num_entry.grid(row=0, column=2, pady=5, padx=2, sticky= "e")

# Barangay Grid
brgy_label.grid(row=0, column=3, pady=5, padx=5, sticky= "e")
brgy_entry.grid(row=0, column=4, pady=5, padx=2)

# City Grid
zip_code_city_label.grid(row=1, column=0, pady=5, padx=5, sticky= "e")
zip_code_entry.grid(row=1, column=1, pady=5, padx=2, sticky=  "w")
city_entry.grid(row=1, column=2, pady=5, padx=2, sticky= "w")

# Province Grid
province_label.grid(row=1, column=3, pady=5, padx=5, sticky= "e")
province_entry.grid(row=1, column=4, pady=5, padx=2)
province_entry.set("Select Province")


# Fifth Frame
fifth_frame = tk.LabelFrame(frame)
fifth_frame.grid(row=4, column=0, sticky= NSEW, pady=5, padx=20)

# Email
email_label = tk.Label(fifth_frame, text= "Email:", font= ("arial normal", 10))
email_entry = tk.Entry(fifth_frame, width= 23)

# Phone Number
phone_num_label = tk.Label(fifth_frame, text= "Phone No.:", font= ("arial normal", 10))
phone_num_entry = tk.Entry(fifth_frame, width= 23)

# Fifth Frame Grid

tk.Label(fifth_frame, text="").grid(row=0, column=0, padx=21)

# Email Grid
email_label.grid(row=0, column=1, pady=5, padx=5, sticky= "e")
email_entry.grid(row=0, column=2, pady=5, padx=2)

tk.Label(fifth_frame, text="").grid(row=0, column=3, padx=19)

# Phone Number Grid
phone_num_label.grid(row=0, column=4, pady=5, padx=5, sticky= "e")
phone_num_entry.grid(row=0, column=5, pady=5, padx=2)


# Terms Frame
terms_frame = tk.LabelFrame(frame)
terms_frame.grid(row=5, column=0, sticky= NSEW, pady=5, padx=20)

accept_var = tk.IntVar()
terms_check = tk.Checkbutton(terms_frame, text= "I accept the terms and conditions.", font= ("arial normal", 10), variable=accept_var)
terms_check.grid(row=0, column=0)


# Data Button
button = tk.Button(frame, text= "Enter Data", command= data_enter, font= ("arial normal", 10))
button.grid(row=6, column=0, sticky= NSEW, pady=10, padx=20)

# Configuration
frame.columnconfigure(0, weight=1)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

window.mainloop()