import socket
from time import ctime
from threading import Thread
import bot

class ClientHandler(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client

        def run(self):
            self._client.send(ctime() + '\nHave a nice day!')
            self._client.close()

def startChat():
    if (clientConnected == 4):
        startingChat = bot.random()
        client_socket.send(startingChat.encode("utf-8"))


HOST = 'localhost'
PORT = 1234
ADDRESS = (HOST, PORT)
BUFFER_SIZE = 1024

print("waiting for exactly 4 bot")
# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Connect to host on port
server_socket.bind((ADDRESS))

# This makes server listen to new connections
server_socket.listen(3)

while True:

    client_socket, address = server_socket.accept()

    print(f"Connection with {address} established")

    handler = ClientHandler(client_socket)
    handler.start()


