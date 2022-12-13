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

The code **client.py**:

This code is a simple client for a socket connection. It imports the socket module and defines some constants for the connection, such as the header size, the port, and the format to use for encoding messages. It then creates a socket and connects to a server using the defined address.

The send() function takes a message as an argument, encodes it in the specified format, and sends it to the server. It also sends the length of the message as a header to the server so that it knows how many bytes to expect in the incoming message. Finally, the code sends two messages to the server, "HELLO world" and the disconnect message.

The code **server.py**:

This code is a server that listens for incoming connections and starts a new thread to handle each client. The server listens on port 7000 and uses the handle_client function to handle each client. The handle_client function receives two parameters: conn (the client's connection object) and addr (the client's address). It reads incoming messages from the client and prints them to the console until the client sends the DISCONNECT_MESSAGE signal. When this happens, the function closes the client's connection and terminates the thread. The start function listens for new connections, creates a new thread for each one, and passes the connection object and address to the handle_client function. It also prints the number of active connections to the console.

### IP calculation

When we are learning about network and IP adresses, can be confusing calculate the ammoung of IP addresses that fit within a determinate mask

The code **IP_Calculator.py**:

This code defines a GUI application that calculates information about an IP address and its mask. The user enters an IP address and a mask in the designated text entry boxes and then clicks the "Calculate" button. This triggers the clicked function, which calls the ip_finder function in the IP_address module, passing it the entered IP address and mask as arguments. The ip_finder function returns a tuple of four strings containing the calculated mask, wildcard,

The code **IP_address.py**:

This code defines the ip_finder function, which takes an IP address and a mask as arguments and calculates various information about the IP address and mask. It first splits the IP address into its four octets and converts the mask to an integer. It then uses the decimal_to_binary function from the Binary module to convert the mask to its binary representation. It then calculates the wildcard, network address, and number of available hosts for the given IP address and mask, and returns a list of strings containing these values. The ip_finder function also uses the binary_to_decimal function from the Binary module to convert the binary representation of the network address to its decimal representation.

The code **Binary.py**:

This code defines two functions, decimal_to_binary and binary_to_decimal, that can be used to convert a decimal number to its binary representation and vice versa. The decimal_to_binary function takes a decimal number as an argument and returns its binary representation as a list of 0s and 1s. The binary_to_decimal function takes a binary number as an argument and returns its decimal representation as an integer. Both functions use a global list bits, which contains the powers of 2 from 128 to 1. This list is used to determine which bits in the binary representation of a number should be 1 and which should be 0.

### Library

Program that read a txt file with a library information and do a search within this information, after that the results are present in a GUI made with Tkinter.

The code **Books.py**: 

  This code defines a GUI application with a search feature that allows users to search for books by title or author. It also provides a feature to add new books to a list of books. The search function takes user input from a text entry box and a dropdown menu to determine whether to search by title or author. It then calls the search function from the search_books module, passing it the selected option and the search query entered by the user. The search function returns a list of books matching the search criteria, which are then displayed in a new window. The new_book function creates a new window that allows the user to enter the details of a new book, which are passed to the book function when the user clicks the "Add book" button. The book function then calls the append_book function in the search_books module to add the new book to the list of books.
  
The code **search_books.py**:

  This code defines two functions, library and search, as well as a helper function append_book. The library function reads a text file called "Libros.txt" and parses the contents to extract the details of each book. It then returns a list of lists, where each inner list contains the details of a single book. The search function takes two arguments: an option that specifies whether to search by title or author, and a search query. It calls the library function to get the list of books and then performs a search based on the selected option and the search query. If the search is successful, it returns the details of the matching book(s). The append_book function takes the details of a new book as arguments and appends them to the "Libros.txt" text file.
