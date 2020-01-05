import socket

print("Start")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9000

    s.bind((host, port))
    s.listen()

    while True:
        client, addr = s.accept()
        print(addr)
        print(client.recv(1024))
        client.send("hello client".encode("utf-8"))
        client.close()

except socket.gaierror:
    print("socket error")