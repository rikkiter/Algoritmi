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
                    if temp.left is None:
                        temp.left = Branch(value)
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Branch(value)
                        return
                    else:
                        temp = temp.right

    def search(self, value: int, branch=None, flag=True):
        if branch is None:
            if flag:
                branch = self.head
            else:
                return f"No {value} in Tree"
        if value == branch.value:
            return value
        if value < branch.value:
            return self.search(value, branch.left, False)
        else:
            return self.search(value, branch.right, False)

    def remove(self, value: int, branch=None):
        if branch is None:
            branch = self.head
        if value == branch.value:
            left = branch.left
            prev.right = branch.right
        if value < branch.value:
            return self.search(value, branch.left)
        else:
            return self.search(value, branch.right)

bt = BinaryTree()
bt.add(5)
bt.add(3)
bt.add(7)
bt.add(9)
print(bt.head.right.value)
print(bt.search(0))