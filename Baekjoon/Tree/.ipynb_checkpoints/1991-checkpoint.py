import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
Tree = {}

for _ in range(N):
    root, left, right = input().split()
    Tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(Tree[root][0])
        preorder(Tree[root][1])

def inorder(root):
    if root != '.':
        inorder(Tree[root][0])
        print(root, end='')
        inorder(Tree[root][1])
        
def postorder(root):
    if root != '.':
        postorder(Tree[root][0])
        postorder(Tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')