import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    for data in [b'holo',b'horo']:
        s.sendto(data, ('127.0.0.1', 8080))
        print(s.recv(1024).decode('utf-8'))
    
