import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 8000))
    s.listen(5)
    print("服务器启动。。。。")

    with s.accept()[0] as conn:
        while True:
            data = conn.recv(1024)
            if data:
                print("from client: {}".format(data.decode()))
                conn.send(data.upper())
            else:
                break


