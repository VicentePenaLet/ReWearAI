import socket

class Client():
    def __init__(self, ip = 'localhost', port = 4002):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))
        self.client.send("Username".encode())

    def send_image(self, path, verbose = False):
        file = open(path, "rb")
        image_data = file.read(2048)
        while image_data:
            if verbose:
                print("sending chunk")
            self.client.send(image_data)
            image_data = file.read(2048)
        file.close()
        self.client.close()

if __name__ == "__main__":
    client = Client()
    client.send_image("test_image.jpg", verbose=True)
