from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen=Tk()
    screen.geometry("375x398")

    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for encryption", fg="white", font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20", bg="black", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=335,height=100)

    # Password entry box
    Label(text="Enter secret key for encryption and decryption",fg="white", font=("calbri", 13)).place(x=10, y=170)

    code=StringVar()
    Entry(textvariable=code, width=24,bd=0,font=("arial", 25),show="*").place(x=10, y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00BD56",fg="white",bd=0,command=decrypt).place(x=200, y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10, y=300)




    screen.mainloop()

main_screen()
