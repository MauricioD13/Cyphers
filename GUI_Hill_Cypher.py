from tkinter import *

window=Tk()    
window.title("Hill Cipher")
window.geometry("500x500")

#Objects
plaintext_label=Label(window,text="Plaintext")
plaintext_txt=Entry(window,width=10)
options=Listbox(window, width=10)

#Location
plaintext_label.grid(row=0, column=0)
plaintext_txt.grid(row=1,column=0)
options.insert(0,"Cifrar")
options.grid(row=1, column=1)