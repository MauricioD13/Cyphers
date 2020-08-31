def search(option,book):
    books = []
    options=int(option)
    book_val=str(book)
    output=[]
    with open("Libros.txt", 'r') as f:
        for line in f:
            info = line.split("-")
            for i in range(len(info)):
                info[i] = info[i].strip()
            books.append(info)
    if options==1:
        for i in range(1,len(books)-1):
            if books[i][0].lower()==book_val.lower():
                #print("Titulo: {} \n Autor: {} \n Genero: {}".format(books[i][0],books[i][1],books[i][2]))
                return books[i][0],books[i][1],books[i][2]
                break
            book01=books[i][0].split()
            for j in book01:
                if book_val.lower()==j.lower():
                    #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0], books[i][1],books[i][2],books[i][3]))
                    output.append(books[i])
        return output
    elif options==2:
        for i in range(1,len(books)-1):
            if books[i][1].lower()==book_val.lower():
                output.append(books[i])
                #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0],books[i][1],books[i][2],books[i][3]))
            book02 = books[i][1].split()
            for j in book02:
                if book_val.lower() == j.lower():
                    #print("Titulo: {} \n Autor: {} \n Genero: {} \n Editorial: {}".format(books[i][0], books[i][1],
                    output.append(books[i])                     
        return output            