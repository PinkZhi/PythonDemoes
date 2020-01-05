import socket
import threading
import queue

class Sender(threading.Thread):
    def __init__(self, socket, queue, lock):
        threading.Thread.__init__(self)
        self.socket = socket
        self.queue = queue
        self.lock = lock

    def run(self):
        self.lock.acquire()
        while not self.queue.empty():
            buf = self.queue.get()
            self.socket.send(buf)

        self.lock.release()