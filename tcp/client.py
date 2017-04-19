import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 8080))
    s.sendall(b'I am Holo')
    s.shutdown(socket.SHUT_WR)

    buffer = []
    while True:
        d = s.recv(4096)
        if not d:
            break
        buffer.append(d)
    data = b''.join(buffer)
    s.close()

print(data.decode('utf-8'))
