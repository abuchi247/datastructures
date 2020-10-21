class Node:
    def __init__(self, data):
        self._data = data
        self._parent = None
        self._left_child = None
        self._right_child = None

    def get_left(self):
        return self.left_child

    def set_left(self, new_left):
        self.left_child = new_left

    def get_right(self):
        return self.right_child

    def set_right(self, new_right):
        self.right_child = new_right

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def get_data(self):
        return self.data
