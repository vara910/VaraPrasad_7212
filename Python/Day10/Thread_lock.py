import threading
import time

def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the lock")

lock = threading.Lock()
threads = []

for i in range(3):  # Creating 3 threads
    thread = threading.Thread(target=task, args=(lock,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to complete
