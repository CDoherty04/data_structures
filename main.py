import time
from queue import Queue

if __name__ == "__main__":

    start_time = time.time()

    my_queue = Queue()

    # How many items will be added and removed from the queue
    iterations = 99999

    for i in range(iterations):
        my_queue.enqueue(i+1)

    for i in range(iterations):
        my_queue.dequeue()

    # Calculate time spent running the program
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(elapsed_time)
