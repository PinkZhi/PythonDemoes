import socket
import threading
import queue

class Recver(threading.Thread):
    def __init__(self, socket, queue, lock):
        threading.Thread.__init__(self)
        self.socket = socket
        self.queue = queue
        self.lock = lock

    def run(self):
        self.lock.acquire()
        while not self.queue.empty():
            buf = self.queue.get()
            self.socket.recv(buf)

        self.lock.release()