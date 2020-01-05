import threading
import queue
import time

lock = threading.Lock()
workQue = queue.Queue(100)

class consume(threading.Thread):
   def __init__(self, threadId, name):
      threading.Thread.__init__(self)
      self.threadId = threadId
      self.name = name

   def run(self):
      print ("开启线程：" + self.name)
      self.conusme()
      print ("退出线程：" + self.name)

   def conusme(self):
      lock.acquire()
      while not workQue.empty():
         n = workQue.get()
         print(n+100)
      lock.release()


class produce(threading.Thread):
   def __init__(self, threadId, name):
      threading.Thread.__init__(self)
      self.threadId = threadId
      self.name = name

   def run(self):
      print ("开启线程：" + self.name)
      self.produce()
      print ("退出线程：" + self.name)
   
   def produce(self):
      for count in range(0, 10):
         lock.acquire()
         print(count)
         workQue.put(count)
         lock.release()
         time.sleep(count)

def main():
   producer = produce(0, "produce")
   producer.start()

   consumer = consume(1, "consume")
   consumer.start()

   producer.join()
   consumer.join()
   return

if __name__ == '__main__':
   main()