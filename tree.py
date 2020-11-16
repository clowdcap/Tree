class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node


if __name__ == "__main__":
    tree = BinaryTree('RAIZ')
    tree.root.left = Node('ESQUERDA')
    tree.root.right = Node('DIREITA')

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
