import socket
import threading
import queue

class CLient_Socket(threading.Thread):
    def __init__(self, host, port):
        try:
            self.stop = False
            threading.Thread.__init__(self)
            self.sendQue = queue.Queue(512)
            self.recvQue = queue.Queue(512)
            self.sendLock = threading.Lock()
            self.recvLock = threading.Lock()
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        except socket.gaierror:
            print("Socket Connect error")
            self.socket = None
        except:
            print("client socket init error")
            self.socket = None

    def close(self):
        self.stop = True
        self.socket.close()
        self.socket = None
