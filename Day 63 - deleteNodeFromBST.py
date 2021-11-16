# Given a Binary Search Tree and a node value X, delete the node with the given value X from the BST
# Day 63/100

def findMinRoot(root, minRoot):
    if not root:
        return

    if root.data <= minRoot[0]:
        minRoot[0] = root.data

    findMinRoot(root.left, minRoot)
    findMinRoot(root.right, minRoot)


def trav(root, X):
    if not root:
        return

    if root.data > X:
        root.left = trav(root.left, X)
    elif root.data < X:
        root.right = trav(root.right, X)
    else:
        if not root.left and not root.right:
            root = None

        elif not root.left:
            temp = root
            root = root.right
            del temp

        elif not root.right:
            temp = root
            root = root.left
            del temp

        else:
            minRoot = [root.right.data]
            findMinRoot(root.right, minRoot)
            root.data = minRoot[0]
            root.right = trav(root.right, minRoot[0])

    return root


def deleteNode(root, X):

    root = trav(root, X)

    return root


#  Driver Code Starts
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" "),
        inorder(root.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        x = int(input())
        root = buildTree(s)
        root = deleteNode(root, x)
        inorder(root)
        print()
