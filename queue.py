from node import Node


class Queue:

    def __init__(self):
        self._top = None

    def enqueue(self, entry):
        """Add to the back"""

        node = Node(entry)

        if self.is_empty():
            self._top = node
        else:
            temp = self._top.next
            while temp is not None:
                s

    def dequeue(self, node):
        """Remove the front"""

        pass

    def peek_front(self):
        """Look at the front node"""

        return self._top

    def is_empty(self):
        """Checks for any nodes in the queue"""

        if self._top is None:
            return False
        return True
