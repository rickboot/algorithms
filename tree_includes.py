from logging.config import valid_ident


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):
    queue = [root]

    print(queue)
    while len(queue) > 0:
        cur = queue.pop(0)

        if cur.val == target:
            return True
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)

    return False


# ----------------------


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

target = 'G'
result = tree_includes(a, target)
print(result)
