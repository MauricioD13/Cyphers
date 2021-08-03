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
                if self.storage[i].title.lower() == word.lower():
                    return self.storage[i].title,self.storage[i].autor,self.storage[i].genre
                
                book01=self.storage[i].title.split()
                
                for j in book01:
                    if word.lower() == j.lower():
                        
                        output.append(self.storage[i])
            return output
        elif option == 2:
            for i in range(len(self.storage)):
                if self.storage[i].title.lower() == word.lower():
                    output.append(self.storage[i])
                    #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0],books[i][1],books[i][2],books[i][3]))
                book02 = self.storage[i].title.split()
                for j in book02:
                    if word.lower() == j.lower():
                        #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0], books[i][1],
                        output.append(self.storage[i])   
                        print(output)                  
            return output
    def view_books(self):
        for i in self.storage:
            print(f"TITLE: {i.title} \t AUTOR: {i.autor} \n GENRE: {i.genre} \t EDITORIAL: {i.editorial}")
            print("------------------------------------------")


    def load_books(self,file_name):
        items =[]
        with open("Libros.txt", 'r') as f:
            for line in f:
                info = line.split("-")
                for i in range(len(info)):
                    info[i] = info[i].strip()
                items.append(info)
        for item in items:
            book = Book(item[0],item[1],item[2],item[3])
            library.new_book(book)    
                 

library = Library("Mi biblioteca")    

library.load_books("Libros.txt")

#library.view_books()

books = []
books = library.search_books("olvido",1)

for book in books:
    print(f"TITLE: {book.title} \t AUTOR: {book.autor} \n GENRE: {book.genre} \t EDITORIAL: {book.editorial}")
    print("------------------------------------------")
