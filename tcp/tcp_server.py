import socket
import threading
import time

def tcplink(sock, addr):
    print('accept new connection form %s:%s' %addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, {}!'.format(data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print('connection closed from %s:%s' %addr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 8080))
    s.listen(5)
    print('wait for connecting...')

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target = tcplink, args = (sock, addr))
        t.start()
