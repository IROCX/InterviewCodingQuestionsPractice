# Given below is a binary tree. The task is to print the top view of binary tree.
# Top view of a binary tree is the set of nodes visible when the tree is viewed from the top
# Day 38/100


from collections import deque
from collections import defaultdict


def defval():
    return -1


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.

    def dfs(self, head, lvl, dp, d):

        if head == None:
            return
        else:
            if lvl < 0:
                if d[lvl] == -1:
                    d[lvl] = [head.data, dp]
                else:
                    if dp < d[lvl][1]:
                        d[lvl] = [head.data, dp]

            elif lvl > 0:
                if d[lvl] == -1:
                    d[lvl] = [head.data, dp]
                else:
                    if dp < d[lvl][1]:
                        d[lvl] = [head.data, dp]

            self.dfs(head.left, lvl-1, dp+1, d)

            self.dfs(head.right, lvl+1, dp+1, d)

    def topView(self, root):
        lvl = 0
        dp = 0

        d = defaultdict(defval)

        self.dfs(root, lvl, dp, d)
        d[0] = [root.data, 0]
        res = []
        for i in sorted(d.keys()):
            res.append(d[i][0])

        return res


#  Driver Code Starts
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
        s = input()
        root = buildTree(s)
        ob = Solution()

        res = ob.topView(root)
        for i in res:
            print(i, end=" ")
        print()
