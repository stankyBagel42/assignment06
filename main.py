import threading
from queue import Queue
from producer import Producer
from consumer import Consumer

count = 0
q = Queue(10)
threadLock = threading.Lock()
threadLst = []


class main:
    def __init__(self, threads, q):
        self.threads = threads
        self.q = q

    def main(self):
        # Tests producer thread
        try:
            for thread in self.threads:
                thread.start()
        except:
            print("Error: unable to start thread")


if __name__ == '__main__':
    threadLst.append(Producer(1, "Thread-1", q, threadLock))
    threadLst.append(Producer(2, "Thread-2", q, threadLock))
    threadLst.append(Consumer(3, "Thread-3", q, threadLock))
    threadLst.append(Consumer(4, "Thread-4", q, threadLock))
    threadLst.append(Consumer(5, "Thread-5", q, threadLock))
    mThread = main(threadLst, q)
    mThread.main()
