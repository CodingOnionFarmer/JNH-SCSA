# 노드 번호를 매기지 않고 알파벳을 바로 Node로 대응시키기 위해 dictionary로 만들었다.


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None


n = int(input())
Tree = {}
for i in range(n):
    a, b, c = input().split()
    node = Node()
    node.value = a
    Tree[a] = node
    if b != '.':
        node.left = b
    if c != '.':
        node.right = c

pre_order = []
in_order = []
post_order = []


def preorder_traverse(alp):
    pre_order.append(alp)
    if Tree[alp].left:
        preorder_traverse(Tree[alp].left)
    if Tree[alp].right:
        preorder_traverse(Tree[alp].right)


def inorder_traverse(alp):
    if Tree[alp].left:
        inorder_traverse(Tree[alp].left)
    in_order.append(alp)
    if Tree[alp].right:
        inorder_traverse(Tree[alp].right)


def postorder_traverse(alp):
    if Tree[alp].left:
        postorder_traverse(Tree[alp].left)
    if Tree[alp].right:
        postorder_traverse(Tree[alp].right)
    post_order.append(alp)


preorder_traverse('A')
inorder_traverse('A')
postorder_traverse('A')

print(*pre_order, sep='')
print(*in_order, sep='')
print(*post_order, sep='')
