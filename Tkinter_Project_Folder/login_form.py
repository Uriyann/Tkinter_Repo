import tkinter as tk
from tkinter import messagebox

main = tk.Tk()
main.title("Login Form")
main.geometry('400x400')
main.configure(bg='gray20')

def login():
    
    username = "Josh"
    password = "123"
    
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        
    else:
        messagebox.showerror(title="Login Failed", message="Wrong Credentials. Try Again.")

frame = tk.Frame(bg='gray20')

login_label = tk.Label(frame, text= "Login", bg="gray20", fg="deeppink", font= ("arial", 30))
username_label = tk.Label(frame, text= "Username:", bg="gray20", fg="white", font= ("arial", 16))
password_label = tk.Label(frame, text= "Password:", bg="gray20", fg="white", font= ("arial", 16))

username_entry = tk.Entry(frame, font= ("arial", 16))
password_entry = tk.Entry(frame, show= "*", font= ("arial", 16))

login_button = tk.Button(frame, text= "Login", font= ("arial", 16), bg="deeppink", fg="white", command= login)



login_label.grid(row="0", column= "0", columnspan= 2, sticky= "news", pady= 40)
username_label.grid(row="1", column= "0")
password_label.grid(row="2", column= "0")

username_entry.grid(row="1",column="1",pady= 10)
password_entry.grid(row="2",column="1",pady= 10)

login_button.grid(row="3",column="0", columnspan= 2, pady= 30)

frame.pack()

main.mainloop()