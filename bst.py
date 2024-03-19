from binarynode import BinaryNode


class BST:

    def __init__(self):
        self._root = None

    def add(self, entry):
        new_node = BinaryNode(entry)
        if self._root is None:
            self._root = new_node

        else:
            self._rec_add(new_node, self._root)

    def _rec_add(self, new_node, cur_node):

        # Check left
        if new_node.entry < cur_node.entry:
            if cur_node is None:
                cur_node = new_node
            else:
                self._rec_add(new_node, cur_node.left)

        # Check right
        elif new_node.entry > cur_node.entry:
            if cur_node is None:
                cur_node = new_node
            else:
                self._rec_add(new_node, cur_node.right)

        else:
            raise RuntimeError("No duplicates allowed within a Binary Search Tree")
