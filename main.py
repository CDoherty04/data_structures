from node import Node
from queue import Queue

if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)

    my_queue.peek_front()
