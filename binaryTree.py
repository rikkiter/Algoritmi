class Branch:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, value: int, branch=None):
        if self.head is None:
            self.head = Branch(value)
            return
        if branch is None:
            branch = self.head
        if value < branch.value:
            if branch.left is None:
                branch.left = Branch(value)
                return
            return self.add(value, branch.left)
        else:
            if branch.right is None:
                branch.right = Branch(value)
                return
            return self.add(value, branch.right)

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

    def remove(self, value: int, branch=None, flag=True):
        if branch is None:
            if flag:
                branch = self.head
            else:
                return f"No {value} in Tree"
        if branch.right is not None and value == branch.right.value:
            if branch.right.right is not None:
                left = branch.right.left
                branch.right.value = branch.right.right.value
                branch.right = branch.right.right
                temp = branch.right
                while True:
                    if temp.left is None:
                        temp.left = left
                        return
                    else:
                        temp = temp.left
            elif branch.right.left is not None:
                branch.right.value = branch.right.left.value
                branch.right = branch.right.left
                return
            else:
                branch.right = None
                return
        if branch.left is not None and value == branch.left.value:
            if branch.left.right is not None:
                left = branch.left.left
                branch.left.value = branch.left.right.value
                branch.left = branch.left.right
                temp = branch.left
                while True:
                    if temp.left is None:
                        temp.left = left
                        return
                    else:
                        temp = temp.left
            elif branch.left.left is not None:
                branch.left.value = branch.left.left.value
                branch.left = branch.left.left
                return
            else:
                branch.left = None
                return
        if value < branch.value:
            return self.remove(value, branch.left, False)
        if value > branch.value:
            return self.remove(value, branch.right, False)

bt = BinaryTree()
for num in [17, 5, 25, 19, 30, 28, 70, 3, 9]:
    bt.add(num)
print(bt.search(0))
print(bt.search(19))
print(bt.search(70))
print(bt.remove(30))
print(bt.search(30))
print(bt.search(70))
print(bt.remove(28))
print(bt.search(19))