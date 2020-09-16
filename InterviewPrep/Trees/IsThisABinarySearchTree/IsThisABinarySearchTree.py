class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,data): 
          self.data = data  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

def checkBST(root):
    print("checkBST({})".format(root))

    if root is None:
        return False

    if root.left is not None and root.left.data < root.data:
        if not checkBST(root.left):
            return False

    if root.right is not None and root.right.data > root.data:
        if not checkBST(root.right):
            return False

    return True



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(tree.root)

if checkBST(tree.root):
    print("Yes")
else:
    print("No")
