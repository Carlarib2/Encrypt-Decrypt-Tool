from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen=Tk()
    screen.geometry("375x398")

    screen.title("PctApp")

    Label(text="Enter text for encryption", fg="white", font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20", bg="black", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=335,height=100)

    Label(text="Enter secret key for encryption and decryption",fg="white", font=("calbri", 13)).place(x=10, y=170)

    code=StringVar()
    Entry(textvariable=code, width=24,bd=0,font=("arial", 25),show="*").place(x=10, y=200)

    screen.mainloop()

main_screen()
