import threading
import queue
import time

def producer(q):
    for i in range(5):
        q.put(i)
        print(f"producing {i}")
        time.sleep(1)
def consumer(q):
    while True:
        item= q.get()
        if item is None:
            break
        print(f"consumiing {item}")
        q.task_done()
    
q= queue.Queue()
producer_thread= threading.Thread(target=producer,args=(q,))
consumer_thread= threading.Thread(target=consumer,args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)
consumer_thread.join()

print("thread communication completed")
