import functions

if __name__ == "__main__":
    # Place function calls here
    print(functions.is_balanced("()"))  # True
    print(functions.is_balanced("("))  # False
    print(functions.is_balanced(")"))  # False
    print(functions.is_balanced("(()"))  # False
    print(functions.is_balanced("(())"))  # True
    print(functions.is_balanced(")(()"))  # False
    print(functions.is_balanced("(()())"))  # True

    print(functions.queue_time_test(1000))  # A split-second
    print(functions.queue_time_test(10000))  # About a second
    print(functions.queue_time_test(100000))  # A long ass time
