class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    data = dict() # horiz pos -> list of (info,height)
    def tv(r,i,h):
        if not r:
            return
        tv(r.left,i-1,h+1)
        tv(r.right,i+1,h+1)
        if i not in data:
            data[i] = []
        data[i].append((r.info,h))
    tv(root,0,0)
    for x in sorted(data.keys()):
        data[x] = sorted(data[x],key=lambda y:y[1])
        print(data[x][0][0],end=' ')



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
