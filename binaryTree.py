class Branch:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, value: int):
        if self.head is None:
            self.head = Branch(value)
            return
        else:
            temp = self.head
            while True:
                if temp.value > value:
                    temp = temp.left
                    if temp is None:
                        temp = Branch(value)
                        return
                else:
                    temp = temp.right
                    if temp is None:
                        temp = Branch(value)
                        return

    def search(self, value: int, branch=None):
        if branch is None:
            branch = self.head
        if value == branch.value:
            return value
        if value < branch.value:
            return self.search(value, branch.left)
        else:
            return self.search(value, branch.right)

bt = BinaryTree()
bt.add(5)
bt.add(3)
bt.add(7)
bt.add(4)
bt.add(9)
print(bt.head.right)
# print(bt.search(3))