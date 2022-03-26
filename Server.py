import socket

class Server():
    def __init__(self, ip = 'localhost', port = 4002):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen(5)
        self.client_socket, self.client_address = self.server.accept()
        username = self.client_socket.recv(2048)
        print(username)
        file = open('received_image.jpg', "wb")
        image_chunk = self.client_socket.recv(2048)

        while image_chunk:
            print("receiving client")
            file.write(image_chunk)
            image_chunk = self.client_socket.recv(2048)

    def close(self):
        self.server.close()

if __name__ == "__main__":
    server = Server()
    #server.close()

