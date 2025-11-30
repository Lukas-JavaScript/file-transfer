import socket

SERVER = input("Enter the server IP address to connect to: ")
PORT = 4444


file_send = input("Enter the file name to send: ")
s = socket.socket()
s.connect((SERVER, PORT))
msg = s.recv(1024).decode()
print('[*] server:', msg)

# Send the file name
s.send(file_send.encode())

# Send the file contents
with open(file_send, 'rb') as f:
    print('[*] Sending file...')
    while True:
        data = f.read(1024)
        if not data:
            break
        s.send(data)

print('[*] File sent successfully.')
s.close()
