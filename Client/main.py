import socket
import _thread

print("Start")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9000

    s.connect((host, port))
    s.send("hello Server".encode("utf-8"))
    print(s.recv(1024))

except socket.gaierror:
    print("socket error")