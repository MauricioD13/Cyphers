import socket

HEADER= 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER=socket.gethostbyname(socket.gethostname())

ADDR= (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT) #Codifica el string en bytes como un objeto
    msg_len=len(message)
    send_length=str(msg_len).encode(FORMAT)
    send_length+= b' ' *(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("HELLO world")
send(DISCONNECT_MESSAGE)