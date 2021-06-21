import threading
from random import Random


class Producer(threading.Thread):
    def __init__(self, threadID, name, queue, threadLock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = queue
        self.lock = threadLock

    def run(self):
        print(f"Starting {self.name}")
        while True:
            # Get lock to synchronize threads
            self.lock.acquire()
            if not self.q.full():
                self.q.put(Random.randint(Random(), 0, 100))
            # Free lock to release next thread
            self.lock.release()



