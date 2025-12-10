import threading
import time

resource_a = threading.Lock()
resource_b = threading.Lock()

def thread_function_1():
    with resource_a:
        print("Thread 1 acquired resource A \n")
        time.sleep(1)
        print("Thread 1 waiting for resource B \n")
        with resource_b:
            print("Thread 1 acquired resource B \n")

def thread_function_2():
    with resource_b: 
        print("Thread 2 acquired resource B \n")
        time.sleep(1)
        print("Thread 2 waiting for resource A \n")
        with resource_a:
            print("Thread 2 acquired resource A \n")

thread1 = threading.Thread(target=thread_function_1)
thread2 = threading.Thread(target=thread_function_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
