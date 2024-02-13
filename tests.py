import time

import linkedlist
import linkedqueue
from stack import Stack
from linkedqueue import LinkedQueue


def is_balanced(parentheses):
    """Given a set of parentheses, check for balance. '(())' or '(()())' are valid examples;
    ')(' or (() are invalid examples"""

    the_stack = Stack()

    for parenthesis in parentheses:

        # Add a parenthesis
        if parenthesis == "(":
            the_stack.push(parenthesis)

        # The parenthesis is closed and there's no unpaired parenthesis
        elif the_stack.is_empty():
            return False

        # If the parenthesis is closed and there's an unpaired parenthesis, pair it
        else:
            the_stack.pop()

    # Ensure there's no extra opening parenthesis
    return the_stack.is_empty()


def queue_time(iterations):
    """Function that adds and removes from a queue based on user given number of iterations"""

    start_time = time.time()
    my_queue = Queue()

    for i in range(iterations):
        my_queue.enqueue(i + 1)

    for i in range(iterations):
        my_queue.dequeue()

    # Calculate time spent running the program
    end_time = time.time()
    elapsed_time = end_time - start_time

    return f"Elapsed time: {elapsed_time}"


def queue_time_test():
    print(queue_time(100000))  # A split-second
    print(queue_time(1000000))  # A half second
    print(queue_time(10000000))  # About 5 seconds


def is_balanced_test():
    print(is_balanced("()"))  # True
    print(is_balanced("("))  # False
    print(is_balanced(")"))  # False
    print(is_balanced("(()"))  # False
    print(is_balanced("(())"))  # True
    print(is_balanced(")(()"))  # False
    print(is_balanced("(()())"))  # True


def queue_access_test():
    my_linked_list = linkedlist.LinkedList()
    my_linked_list.insert(0, "B")
    my_linked_list.insert(0, "A")
    my_linked_list.insert(2, "D")
    my_linked_list.insert(2, "C")
    my_linked_list.insert(4, "E")

    print(my_linked_list.get_entry(1))  # Should access "B"
    print(my_linked_list.get_entry(3))  # Should access "D"
    print(my_linked_list.get_entry(2))  # Should access "C"
    print(my_linked_list.get_entry(0))  # Should access "A"
    print(my_linked_list.get_entry(5))  # Should raise IndexError


def run():
    # Place function calls here
    # queue_time_test()
    # is_balanced_test()
    queue_access_test()
