from tkinter import *
from tkinter import ttk
import Hill_Cipher
window=Tk()
    
window.title("Hill Cipher")
window.geometry("500x500")

def clicked():
    information=[]
    if action_options.get()=="Cifrar":
       information=Hill_Cipher.preparation("ebdacbfbd",text_txt.get())
       mensaje=Hill_Cipher.Encryption(information)
       result_label.configure(text=mensaje)
    else:
        information=Hill_Cipher.preparation("ebdacbfbd",text_txt.get())
        mensaje=Hill_Cipher.Decryption(information)
        result_label.configure(text=mensaje)
#Objects
text_label=Label(window,text="Plaintext")
text_txt=Entry(window,width=20)
action_options=ttk.Combobox(window,width=15)
empty0=Label(window,text="      ")
btn=Button(window, text="Calculate", command=clicked)
result_label=Label(window,text="---------")
options=["Cifrar","Descifrar"]
action_options['values']=options

#Location
text_label.grid(row=0, column=0)
text_txt.grid(row=1,column=0)
action_options.grid(row=1, column=2)
empty0.grid(row=1, column=1)
btn.grid(row=1,column=3)
result_label.grid(row=2,column=2)


window.mainloop()