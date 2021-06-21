import threading


class Consumer(threading.Thread):
    def __init__(self, threadID, name, queue, threadLock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = queue
        self.lock = threadLock

    def run(self):
        print(f"Starting {self.name}")
        while True:
            self.lock.acquire()
            if not self.q.empty():
                item = self.q.get()
                print(f"Consumer: {item}")
            self.lock.release()
