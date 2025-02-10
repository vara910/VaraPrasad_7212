import threading
import time 
def process_data(data):
    results=sum(data)
    print(f"the sum of data",{results})
data_chunks=[
    list(range(10)),
    list(range(20,30)),
    list(range(30,40))
    ]
threads=[]
for data in data_chunks:
    thread1=threading.Thread(target=process_data, args=(data,))
    threads.append(thread1)
    thread1.start()
for thread1 in threads:
    thread1.join()