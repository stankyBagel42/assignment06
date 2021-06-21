import threading
from producer import Producer
from consumer import Consumer

count = 0
q = []
threadLock = threading.Lock()
thread = []

class main():
  def __init__(self, threads, q):
    self.threads = threads
    self.q = q

  def main(self):
    #Tests producer thread
    try:
      for thread in self.threads:
        thread.start()
    except:
      print("Error: unable to start thread")
      
    