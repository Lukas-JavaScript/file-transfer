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

    try:
        # Receive the file name
        file_name = client[0].recv(1024).decode()
        print(f'[+] Received file name: {file_name}')

        # Validate the file name
        if not file_name:
            print("[!] No file name received. Closing connection.")
            client[0].close()
            continue
    except UnicodeDecodeError:
        print("[!] Failed to decode file name. Closing connection.")
        client[0].close()
        continue

    # Open the file to write binary data
    with open(file_name, 'wb') as f:
        print('[*] Receiving file...')
        while True:
            data = client[0].recv(1024)
            if not data:
                break
            f.write(data)

    print(f'[+] File {file_name} received successfully.')
    client[0].close()

    cmd = input('Wait for new client y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break
s.close()
