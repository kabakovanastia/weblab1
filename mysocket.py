import socket
import keyboard

class DataTransferClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    def send_direction(self):
        key = keyboard.read_key()
        if key == 'left':
            key = '0'
        elif key == 'up':
            key = '1'
        elif key == 'right':
            key = '2'
        elif key == 'down':
            key = '3'

        if key in ['0', '1', '2', '3']:
            self.sock.send(str.encode(key))


class DataTransferServer:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', self.port))
        self.sock.listen()
        self.conn, self.addr = self.sock.accept()
        print(f'client connected ip: {self.addr}')

    def recv_direction(self):
        key = self.conn.recv(1024).decode()[0]
        print(key)

        if key == '0':
            key = 'Left'
        elif key == '1':
            key = 'Up'
        elif key == '2':
            key = 'Right'
        elif key == '3':
            key = 'Down'

        return key

    def __del__(self):
        self.conn.close()
