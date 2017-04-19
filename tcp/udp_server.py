import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 8080))
    print('bind 8080...')
    while True:
        data, addr = s.recvfrom(1024)
        print('Recevied from %s:%s' %addr)
        s.sendto(b'Hello %s' %data, addr)
