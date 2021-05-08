import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 8000))

    while True:
        msg = input('>>>')
        if msg:
            s.send(msg.encode())
            data = s.recv(1024)
            print('from server: {}'.format(data.decode()))
        else:
            break
