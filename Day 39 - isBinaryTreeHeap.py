# Given a binary tree you need to check if it follows max heap property or not
# Day 39/100


from collections import deque
import sys


class Solution:

    def isHeap(self, head):
        q = list()
        if not head:
            return 0

        q.append(head)
        last = 0
        flag = 0
        while q:
            temp = q.pop(0)

            if last == 1 and (temp.left or temp.right):
                flag = 1
                break

            if temp.left and temp.right:
                if temp.data < temp.left.data:
                    flag = 1
                    break
                q.append(temp.left)

                if temp.data < temp.right.data:
                    flag = 1
                    break
                q.append(temp.right)

            elif temp.left:
                last = 1
                if temp.data < temp.left.data:
                    flag = 1
                    break
                q.append(temp.left)

            elif temp.right:
                flag = 1
                break
            else:
                last = 1

        return False if flag == 1 else True


#  Driver Code Starts
sys.setrecursionlimit(10**6)
# Tree Node


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
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
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        root = buildTree(input())
        ob = Solution()
        if ob.isHeap(root):
            print(1)
        else:
            print(0)
