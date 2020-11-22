from tkinter import *
from app import  Register_User

def Register():
    screen1 = Tk()
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()
    Label(screen1 , text = "Username ").pack()
    username_entry = Entry(screen1 , textvariable = username)
    username_entry.pack()
    Label(screen1 , text = "Password ").pack()
    password_entry = Entry(screen1 , textvariable = password)
    password_entry.pack()
    Label(screen1 , text ="").pack()
    Button(screen1 ,  text = "Register" , height = "2" , width = "30" , command = Register_User).pack()
