# Python-programs
Is a python code that encrypt message, also have GUI with tkinter

## Projects

Each directory correspond to a project develop in python using diferents libraries 


### Ciphers

This project is about doing some ciphers with Python in this case the ciphers are symmetic:

- Caesar: Rotate the message letters by an amount of letters that are the key in this cipher
- Vigenere: Rotate the message letters by an amount of letters and rotate the alphabet each letter
- Hill Cipher: Using the properties of matricial algebra encrypt a message with a password 

### Music

Make a downloader of Youtube where it organized the music, all of this with the help of a library call youtube_dl 

### Networking

The inspiration of learning how to make a server in python, resulted in making a program that act like a server and other like the client to probe TCP connection between them.

### IP calculation

When we are learning about network and IP adresses, can be confusing calculate the ammoung of IP addresses that fit within a determinate mask

### Library

Program that read a txt file with a library information and do a search within this information, after that the results are present in a GUI made with Tkinter.

The code Books.py: 
  This code defines a GUI application with a search feature that allows users to search for books by title or author. It also provides a feature to add new books to a list of books. The search function takes user input from a text entry box and a dropdown menu to determine whether to search by title or author. It then calls the search function from the search_books module, passing it the selected option and the search query entered by the user. The search function returns a list of books matching the search criteria, which are then displayed in a new window. The new_book function creates a new window that allows the user to enter the details of a new book, which are passed to the book function when the user clicks the "Add book" button. The book function then calls the append_book function in the search_books module to add the new book to the list of books.
  
The code search_books.py:
  This code defines two functions, library and search, as well as a helper function append_book. The library function reads a text file called "Libros.txt" and parses the contents to extract the details of each book. It then returns a list of lists, where each inner list contains the details of a single book. The search function takes two arguments: an option that specifies whether to search by title or author, and a search query. It calls the library function to get the list of books and then performs a search based on the selected option and the search query. If the search is successful, it returns the details of the matching book(s). The append_book function takes the details of a new book as arguments and appends them to the "Libros.txt" text file.
