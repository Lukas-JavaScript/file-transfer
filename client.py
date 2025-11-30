import socket

SERVER = input("Enter the server IP address to connect to: ")
PORT = 4444


file_send = input("Enter the file name to send: ")
s = socket.socket()
s.connect((SERVER, PORT))
msg = s.recv(1024).decode()
print('[*] server:', msg)

with open(file_send, 'rb') as f:
    print('[*] Sending file...')
    s.send(f.name.encode())
    data = f.read(1024)
    s.send(data)

s.close()
