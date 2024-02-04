import time
from stack import Stack
from queue import Queue


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


def queue_time_test(iterations):
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
