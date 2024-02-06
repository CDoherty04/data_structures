import functions
import queue

if __name__ == "__main__":
    # Place function calls here
    print(functions.is_balanced("()"))  # True
    print(functions.is_balanced("("))  # False
    print(functions.is_balanced(")"))  # False
    print(functions.is_balanced("(()"))  # False
    print(functions.is_balanced("(())"))  # True
    print(functions.is_balanced(")(()"))  # False
    print(functions.is_balanced("(()())"))  # True

    print(functions.queue_time_test(100000))  # A split-second
    print(functions.queue_time_test(1000000))  # A half second
    print(functions.queue_time_test(10000000))  # About 5 seconds

    my_queue = queue.Queue()
    print(my_queue.peek_front())  # None
    my_queue.enqueue(1)
    print(my_queue.peek_front())  # 1
    my_queue.dequeue()
    print(my_queue.peek_front())  # None
    my_queue.enqueue(2)
    print(my_queue.peek_front())  # 2
    my_queue.enqueue(1)
    print(my_queue.peek_front())  # 2
    my_queue.dequeue()
    print(my_queue.peek_front())  # 1
