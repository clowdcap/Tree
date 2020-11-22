import random

ROOT = "root"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._size = 0

    # Complexidade O[1]
    def push(self, elemento):  # Insere um elemento na pilha
        node = Node(elemento)
        if self.ultimo is None:
            self.ultimo = node
        else:
            self.ultimo.next = node
            self.ultimo = node

        if self.primeiro is None:
            self.primeiro = node

        self._size = self._size + 1

    # Complexidade O[1]
    @property
    def pop(self):  # remove o elemento do topo da pilha
        if self._size > 0:
            elemento = self.primeiro.data
            self.primeiro = self.primeiro.data
            if self.primeiro is None:
                self.ultimo = None
            self._size = self._size - 1
            return elemento
        raise IndexError("A fila está vazia")

    # Complexidade O[1]
    def peek(self):  # retorna o topo sem remover (Observar)
        if self._size > 0:
            elemento = self.primeiro.data
            return elemento
        raise IndexError("A fila está vazia")

    def __len__(self):  # Retorna o tamanho da lista
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            ponteiro = self.primeiro
            while ponteiro:
                r = r + str(ponteiro.data) + " "
                ponteiro = ponteiro.next
            return r
        return "A fila está vazia"

    def __str__(self):
        return self.__repr__()


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Root simboliza raiz da árvore

    # Percurso em ordem simetrica ( Travessia_simétrica() )
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        fila = Fila()
        fila.push(node)
        while len(fila):
            node = fila.pop()
            if node.left:
                fila.push(node.left)
            if node.right:
                fila.push(node.right)
            print(node, end=" ")


class BinarySearchTree(BinaryTree):
    def insert(self, elemento):
        parent = None
        x = self.root
        while x:
            parent = x
            if elemento < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(elemento)
        elif elemento < parent.data:
            parent.left = Node(elemento)
        else:
            parent.right = Node(elemento)

    def search(self, elemento):
        return self._search(elemento, self.root)

    def _search(self, elemento, node):
        if node == 0:
            node = self.root
        if node is None:
            return node
        if node.data == elemento:
            return BinarySearchTree(node)
        if elemento < node.data:
            return self._search(elemento, node.left)
        return self._search(elemento, node.right)


if __name__ == "__main__":

    random.seed(40)


    def random_tree(_size=42):
        elemento = random.sample(range(1, 1000), 42)
        tree = BinarySearchTree()
        for v in elemento:
            tree.insert(v)
        return tree


    def example_tree():
        elemento = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
        tree = BinarySearchTree()
        for v in elemento:
            tree.insert(v)
        return tree


    bst = example_tree()
    bst.inorder_traversal()
    print('\n-----')
    bst.levelorder_traversal()

# SISTEMA DE BUSCA
# print('\n-----')
# items = [30, 33, 55, 61, 117]
# for item in items:
#    tree = BinarySearchTree()
#    r = tree.search(item)
#    if r is None:
#        print('Elemento', item, 'não encontrado')
#    else:
#        print('Elemento', r.root.data, 'foi encontrado')

""" if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n4.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_traversal()
    print('')

tree = BinaryTree('RAIZ')
tree.root.left = Node('ESQUERDA')
tree.root.right = Node('DIREITA')

print(tree.root)
print(tree.root.left)
print(tree.root.right)

# exemplo 2
if __name__ == "__main__":
    tree = postorder_exemple_tree()
    print("Percurso em pós ordem:")
    tree.postorder_traversal()
    print('Altura: ', tree.height())"""

'''
def search(self, elemento, node=0):
    if node == 0:
        node = self.root
    if node is None or node.data == elemento:
        return BinarySearchTree(node)
    if elemento < node.data:
        return self.search(elemento, node.left)
    return self.search((elemento, node.right))


def postorder_exemple_tree():
    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree


    if __name__ == "__main__":
    random.seed(40)

    elemento = random.sample(range(1, 1000), 38)

    bst = BinarySearchTree()
    for v in elemento:
        bst.insert(v)

    bst.inorder_traversal()

    items = [30, 33, 55, 61, 117]
    for item in items:
        r = bst.search(item)
        if r is None:
            print('Elemento', item, 'não encontrado')
        else:
            print('Elemento', r.root.data, 'foi encontrado')'''
