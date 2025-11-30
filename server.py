import socket

SERVER = input("Enter the server IP address to bind to: ")
PORT = 4444

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))

s.listen(1)

while True:
    print(f'[*] listening as {SERVER}:{PORT}')

    client = s.accept()
    print(f'[+] client connected {client[1]}')

    client[0].send('connected'.encode())
    data = client[0].recv(1024).decode()
    print(data)
    file_name = data

    # Validate the file name
    if not file_name:
        print("[!] No file name received. Closing connection.")
        client[0].close()
        continue

    with open(file_name, 'wb') as f:
        print('[*] Receiving file...')
        data = client[0].recv(1024)
        if not data:
            break
        f.write(data)
    client[0].close()

    cmd = input('Wait for new client y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break
s.close()
