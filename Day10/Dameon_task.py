import threading
import time
def demeon_task():
    while True:
        print("daemon thread is running...")
        time.sleep(1)
d=threading.Thread(target=demeon_task, daemon=True)
d.start()
time.sleep(5)
print("main thread existing")