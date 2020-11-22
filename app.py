from tkinter import *
import os
import sys
from Register import *


while True:

  #=====fonction pour Quiter le programme=========   
  def iEXIT():
    sys.exit()
    exit()


  #============fermer la fenetre1(screen1)==========
  def delete1():
    screen1.destroy()


  #============fermer la fenetre2(screen2)==========
  def delete2():
    screen2.destroy()

  #============fermer la fenetre3(screen3)==========     
  def delete3():
    screen3.destroy()  


  #============fermer la fenetre4(screen4)==========
  def delete4():
    screen4.destroy()  






  #===========Entrer les cordoonnees pour inscrire sur la platforme======
  def Register():
    global screen1
    screen1 = Tk()
    screen1.title("*REGISTER*")
    screen1.geometry("400x300")

    global username
    global password
    global email

    global username_entry
    global password_entry
    global email_entry

        
    username = StringVar()
    password = StringVar()
    email = StringVar()

    Label(screen1 , text = "Username ").pack()
    username_entry = Entry(screen1 , textvariable = username)
    username_entry.pack()
    Label(screen1 , text = "Password ").pack()
    password_entry = Entry(screen1 , textvariable = password)
    password_entry.pack()
    Label(screen1 , text = "email ").pack()
    email_entry = Entry(screen1 , textvariable = email)
    email_entry.pack()
    Label(screen1 , text ="").pack()
    Button(screen1 ,  text = "Register" , height = "2" , width = "30" , command = Register_User).pack()
    Label(screen1 , text ="").pack()
    Button(screen1 ,  text = "BACK" , height = "2" , width = "30" , command = delete1).pack()
    Button(screen1 ,  text = "EXIT" , height = "2" , width = "30" , command = iEXIT).pack()




  #====================creer un fichier avec un nom d'utilisateur et ajouter les cordoonnees============= 
  def Register_User():

    global screen2
    screen2 = Toplevel(screen1)


    username_info = username_entry.get()
    password_info = password_entry.get()
    email_info = email_entry.get()

    print(username_info)
    print(password_info)
    print(email_info)
    try :

        file1 = open(username_info+".txt","r")
        file1.close()    
        screen2.title("*REGISTRATION_FAILED*")
        screen2.geometry("400x300")
        print 'Error'
        Label(screen2 , text ="Username Already Used " , fg = "red" ).pack()
        Label(screen2 , text ="Try Another Username", fg = "red" ).pack()
        Label(screen2 , text ="").pack()
        Button(screen2 ,  text = "OK" , height = "2" , width = "30" , command = delete2).pack()

    except:
        print 'ok'
        screen2.title("*REGISTRATION_SUCCESS*")
        screen2.geometry("400x300")
        file = open(username_info+".txt","w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(email_info + "\n")
        file.close()
        Label(screen2 , text ="Registration Success" , fg = "green" ).pack()
        Label(screen2 , text ="").pack()
        Label(screen2 , text ="Your Username Is : "+username_info , fg = "green" ).pack()
        Label(screen2 , text ="Your Password Is : "+password_info, fg = "green" ).pack()
        Label(screen2 , text ="Your E_mail Is : "+email_info, fg = "green" ).pack()
        Label(screen2 , text ="").pack()  
        Button(screen2 , text = "Login" , height = "2" , width = "30" , command= Login).pack()
        Button(screen2 ,  text = "EXIT" , height = "2" , width = "30" , command = iEXIT).pack()
        Button(screen2 ,  text = "OK" , height = "2" , width = "30" , command = delete2).pack()



  def session():

    screen0 = Toplevel(screen1)
    screen0.title("*REGISTRATION_SUCCESS*")
    screen0.geometry("400x300")
    Label(screen0 , text ="Login Success" , fg = "green" ).pack()
    Label(screen0 , text ="username : " +username_info_login , fg = "green" ).pack()
    Label(screen0 , text ="E_mail : " +email_info_login , fg = "green" ).pack()
    Button(screen0 ,  text = "OK" , height = "1" , width = "10" , command = delete4).pack()
    Button(screen0 ,  text = "Profile" , height = "1" , width = "10" , command = delete4).pack()
    Button(screen0 ,  text = "Configuration" , height = "1" , width = "10" , command = delete4).pack()
    Button(screen0 ,  text = "Help" , height = "1" , width = "10" , command = delete4).pack()
    print("LOGIN_SUCCESS")


  #================================LOGIN======pour Entrer les cordoonnees========
  def Login():

    global screen3
    print("Login Session Started")
    screen3 = Tk()
    screen3.geometry("400x300")
    screen3.title("*LOGIN*")

    global username
    global password
    global email
    global username_entry
    global password_entry
    global email_entry

        
    username = StringVar()
    password = StringVar()
    email = StringVar()


    Label(screen3 ,text = "LOGIN" , bg = "gray")
    Label(screen3 , text = "Login Page \n").pack()
    Label(screen3 , text = "Username ").pack()
    username_entry = Entry(screen3 , textvariable = username)
    username_entry.pack()
    Label(screen3 , text = "Password ").pack()
    password_entry = Entry(screen3 , textvariable = password)
    password_entry.pack()
    Label(screen3 , text = "email ").pack()
    email_entry = Entry(screen3 , textvariable = email)
    email_entry.pack()
    Button(screen3 ,  text = "LOGIN" , height = "2" , width = "30" , command = Login_user).pack()
    Label(screen3 , text ="").pack()
    Button(screen3 ,  text = "BACK" , height = "1" , width = "20" , command = delete3).pack()
    Button(screen3 ,  text = "EXIT" , height = "1" , width = "20" , command = iEXIT).pack()








  #=========================LOGIM_USER===pour verifier les cordonner est acceder au profile=============== 
  def Login_user():
    global screen4
    screen4 = Toplevel(screen3)
    screen4.title("*LOGIN_SUCCESS*")
    screen4.geometry("400x250")
    username_info_login = username_entry.get()
    password_info_login = password_entry.get()
    email_info_login = email_entry.get()
    print(username_info_login)
    print(password_info_login)
    print(email_info_login)
    try:
        file = open(username_info_login+".txt","r")
        verify = file.read().splitlines() 
        if password_info_login  in verify and email_info_login in verify  :

            Label(screen4 , text ="Login Success" , fg = "green" ).pack()
            Label(screen4 , text ="username : " +username_info_login , fg = "green" ).pack()
            Label(screen4 , text ="E_mail : " +email_info_login , fg = "green" ).pack()
            Button(screen4 ,  text = "OK" , height = "1" , width = "10" , command = delete4).pack()
            Button(screen4 ,  text = "Profile" , height = "1" , width = "10" , command = delete4).pack()
            Button(screen4 ,  text = "Configuration" , height = "1" , width = "10" , command = delete4).pack()
            Button(screen4 ,  text = "Help" , height = "1" , width = "10" , command = delete4).pack()    
            print("LOGIN_SUCCESS")
        else:

            screen4.title("*LOGIN_SUCCESS*")
            screen4.geometry("400x250")
            screen4.title("LOGIN FAILED")
            Label(screen4 , text ="username OR password incorrect" , fg = "red" ).pack()
            Button(screen4 ,   text = "Login" , height = "2" , width = "30" , command= Login).pack()
            Button(screen4 ,  text = "OK" , height = "2" , width = "30" , command = delete4).pack()
            
        
    except:
        screen4 = Toplevel(screen3)
        screen4.title("LOGIN FAILED")
        Label(screen4 , text ="username OR password incorrect" , fg = "red" ).pack()
        Button(text = "Login" , height = "2" , width = "30" , command= Login).pack()
        Button(screen4 ,  text = "OK" , height = "2" , width = "30" , command = delete4).pack()

    Button(screen4 ,  text = "EXIT" , height = "1" , width = "10" , command = iEXIT).pack()



#=====================================================================================





  #=======================main fonction(la fonction de la premiere page (l'accuille))==========================

  def main_screen():
    screen = Tk()
    screen.geometry("400x300")
    screen.title("*NOTES 1.0*")
    Label(screen ,  text = "NOTES 1.0" , bg = "gray")
    Label(screen , text = "").pack()
    Label(screen , text = "Welcome \n").pack()
    Label(screen , text = "").pack()
    Button(screen , text = "Login" , height = "2" , width = "30" , command= Login).pack()
    Label(screen , text = "").pack()
    Button(screen , text = "Register" , height = "2" , width = "30" , command = Register).pack()
    Button(screen ,  text = "EXIT" , height = "2" , width = "30" , command = iEXIT).pack()

    screen.mainloop()
  

  #===============appeller la fonction main===============
  main_screen()
