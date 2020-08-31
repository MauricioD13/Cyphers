# -*- coding: utf-8 -*-
from tkinter import*
from tkinter import ttk,font,scrolledtext
import search_books

window=Tk()
def search():
    books=[]
    if(option_selection.get()=="Titulo"):
            option=1
    else:
            option=2
    books=search_books.search(option,txt_entry.get())
    new_window=Toplevel(window)
    result_tittle=[]
    result_autor=[]
    result_genre=[]
    result_editorial=[]
    result_tittle_label=Label(new_window,text="Titulo ",fg="white",bg="black",width=30)
    result_autor_label=Label(new_window,text="Autor ",fg="white",bg="black",width=30)
    result_genre_label=Label(new_window,text="Genero ",fg="white",bg="black",width=30)
    result_editorial_label=Label(new_window,text="Editorial",fg="white",bg="black",width=30)
    result_tittle_label.grid(row=0,column=0)
    result_autor_label.grid(row=0,column=1)
    result_genre_label.grid(row=0,column=2)
    result_editorial_label.grid(row=0,column=3)
    print(len(books))
    for i in range(len(books)):
        result_tittle.append(Label(new_window,text=books[i][0],width=30))
        result_autor.append(Label(new_window,text=books[i][1],width=30))
        result_genre.append(Label(new_window,text=books[i][2],width=30))
        result_editorial.append(Label(new_window,text=books[i][3],width=30))
    for j in range(len(books)):
        result_tittle[j].grid(row=j+1,column=0)
        result_autor[j].grid(row=j+1,column=1)
        result_genre[j].grid(row=j+1,column=2)
        result_editorial[j].grid(row=j+1,column=3)
        


#Objects
option_label=Label(window,text="Busqueda por: ")
txt_label=Label(window,text="Palabra clave: ")
txt_entry=Entry(window)
search_btn=Button(window, text="Buscar",command=search)
option_selection=ttk.Combobox(window,width=15)




option_selection['values']=["Titulo","Autor"]


#Location
option_label.grid(row=0,column=0)
option_selection.grid(row=0,column=1)

txt_label.grid(row=1,column=0)
txt_entry.grid(row=1,column=1)
search_btn.grid(row=2,column=1)


window.mainloop()


