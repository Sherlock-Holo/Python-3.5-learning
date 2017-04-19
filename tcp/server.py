import socket
import threading

def server(sock, addr):
    print('connection from %s:%s' %addr)

    buffer = []
    while True:
        d = sock.recv(4096)
        if not d:
            break
        buffer.append(d)
    data = b''.join(buffer)
    print(data.decode('utf-8'))

    with open('server.py', 'r') as f:
        fd = f.read()

    sock.send(fd.encode('utf-8'))
    sock.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 8080))
    s.listen(5)

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target = server, args = (sock, addr))
        t.start()
