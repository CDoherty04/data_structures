from node import Node
from queue import Queue

if __name__ == "__main__":
    my_queue = Queue()

    print(my_queue.peek_front())
    my_queue.enqueue(1)
    print(my_queue.peek_front())
    my_queue.dequeue()
    print(my_queue.peek_front())
    my_queue.enqueue(1)
    print(my_queue.peek_front())
    my_queue.enqueue(2)
    print(my_queue.peek_front())
    my_queue.dequeue()
    print(my_queue.peek_front())
