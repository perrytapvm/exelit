import time
import threading

def worker(name, duration):
    print(f"{name} starting.")
    time.sleep(duration)
    print(f"{name} done after {duration} seconds.")

# Create and start threads
thread1 = threading.Thread(target=worker, args=("Worker 1", 2))
thread2 = threading.Thread(target=worker, args=("Worker 2", 4))

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both workers are done.")
