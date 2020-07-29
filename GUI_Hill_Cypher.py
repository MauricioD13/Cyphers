from tkinter import *
from tkinter import ttk
import Hill_Cipher
window=Tk()
    
window.title("Hill Cipher")
window.geometry("500x500")

def clicked():
    information=[]
    if action_options.get()=="Cifrar":
       if key_select.get()==0: 
            information=Hill_Cipher.preparation(key_txt.get(),text_txt.get())
       else:
            information=Hill_Cipher.preparation("ebdacbfbd",text_txt.get())
       mensaje=Hill_Cipher.Encryption(information)
       result_label.configure(text=mensaje)
    else:
        if key_select.get()==0: 
            information=Hill_Cipher.preparation(key_txt.get(),text_txt.get())
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
key_select=IntVar()
key_select_label=Label(window,text="Desea ingresar su propia clave?")
key_select_radiobtn0=Radiobutton(window,text="Si",variable=key_select,value=0)
key_select_radiobtn1=Radiobutton(window,text="No",variable=key_select,value=1)
key_label=Label(window,text="Llave")
key_txt=Entry(window,width=20)

#Location
text_label.grid(row=0, column=0)
text_txt.grid(row=1,column=0)
action_options.grid(row=1, column=2)
empty0.grid(row=1, column=1)
btn.grid(row=1,column=3)
result_label.grid(row=2,column=3)
key_select_label.grid(row=2, column=0)
key_select_radiobtn0.grid(ipady=2)
key_select_radiobtn1.grid(ipady=3)
key_label.grid(row=2, column=1)
key_txt.grid(row=3,column=1)
window.mainloop()