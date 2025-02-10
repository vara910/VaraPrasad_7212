import threading
import time
print("main thread execution has started")
def single_task():
    print("task for even number iteration")
    n=int(input("enter number of iterations:"))
    for i in range(n):
        a=int(input("enter the number"))
        if a%2==0:
            print(f"{a} it is a even number")
        else:
            print(f"{a} it is an odd nuber")
    time.sleep(5)
    print("sub task is completed")

# def task():
#     print("this is the second task")
#     time.sleep(2)
#     print("task 2 has been finished")
thread1=threading.Thread(target=single_task)

thread1.start()

thread1.join()

print("main thread execution has been done successfully")