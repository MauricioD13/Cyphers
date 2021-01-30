import search_books
class Book():
    def __init__(self,title,autor,genre,editorial):
        self.title = title
        self.autor = autor
        self.genre = genre
        self.editorial = editorial
class Library:
    def __init__(self,name):
        self.title = name
        self.storage = []
    def new_book(self,book):
        self.storage.append(book)
    def search_books(self,word,option):
        output = []
        if option == 1: #Search by title
            for i in range(len(self.storage)):
                if self.storage[i].title.lower()==word.lower():
                    return books[i].title,books[i].autor,books[i].genre
                    break
            book01=self.storage[i].title.split()
            for j in book01:
                if word.lower()==j.lower():
                    output.append(self.storage[i])
        return output
        if option == 2:
            for i in range(len(books)-1):
            if books[i][1].lower()==book_val.lower():
                output.append(books[i])
                #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0],books[i][1],books[i][2],books[i][3]))
            book02 = books[i][1].split()
            for j in book02:
                if book_val.lower() == j.lower():
                    #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0], books[i][1],
                    output.append(books[i])                     
        return output
    def view_books(self):
        for i in self.storage:
            print(f"TITLE: {i.title} \t AUTOR: {i.autor} \n GENRE: {i.genre} \t EDITORIAL: {i.editorial}")
            print("------------------------------------------")


    def load_books(self,file_name):
        items =[]
        items = search_books.library()
        for item in items:
            book = Book(item[0],item[1],item[2],item[3])
            library.new_book(book)

        
                
            
            
                 

library = Library("Mi biblioteca")    

library.load_books("Libros.txt")

library.view_books()
library.search_books("El olvido",1)