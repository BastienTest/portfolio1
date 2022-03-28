import socket
import sys
import bot

whichbot = sys.argv[1]



IP = "127.0.0.1"
PORT = 1234
BUFFER_SIZE = 1024
# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to a given ip and port
client_socket.connect((IP, PORT))
msg = client_socket.recv(BUFFER_SIZE)

if whichbot == "Alice":
    messageToReply = bot.alice(msg)
    client_socket.send(messageToReply.encode("utf-8"))
elif whichbot == "bob":
    messageToReply = bot.bob(msg)
    client_socket.send(messageToReply.encode("utf-8"))
elif whichbot == "dora":
    messageToReply = bot.dora(msg)
    client_socket.send(messageToReply.encode("utf-8"))
elif whichbot == "chuck":
    messageToReply = bot.chuck(msg)
    client_socket.send(messageToReply.encode("utf-8"))
else:
    messageToReply = bot.random()
    client_socket.send(messageToReply.encode("utf-8"))

print("received data", msg)
client_socket.send("hey back".encode("utf-8"))

# data = client_socket.recv(BUFFER_SIZE)
# print("received data:", data)



