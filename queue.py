from node import Node


class Queue:

    def __init__(self):
        self._front = self._rear = None

    def enqueue(self, entry):
        """Add to the back"""

        node = Node(entry)

        if self.is_empty():
            self._front = node
            self._rear = node

        # Only one item in queue
        elif self._front == self._rear:
            self._rear = node
            self._rear.next = self._front

        # Multiple items in queue
        else:
            temp = self._rear
            self._rear = node
            self._rear.next = temp

    def dequeue(self):
        """Remove the front"""

        # One or no items in the queue
        if self._front == self._rear:
            self._front = self._rear = None

        # Multiple items in queue
        else:
            # Use a placeholder node to replace the front
            temp = self._rear
            while temp.next is not self._front:
                temp = temp.next
            self._front = temp

    def peek_front(self):
        """Look at the front node"""

        if self._front:
            return self._front.value
        else:
            return None

    def is_empty(self):
        """Checks for any nodes in the queue"""

        if self._front is None:
            return True
        return False
