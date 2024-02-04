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

        # If the parenthesis is closed and there's an unpaired parenthesis, pair it
        elif the_stack.peek() == "(":
            the_stack.pop()

        # If there's an extra closing parenthesis, return False
        else:
            return False

    # Ensure there's no extra opening parenthesis
    if the_stack.is_empty():
        return True
    return False


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
