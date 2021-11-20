# Houses are arranged in the form of a binary tree. You are standing at target node initially. 
# Find the sum of all nodes within a maximum distance k from target node. The target node should be included in the sum.
# Day 67/100


from collections import defaultdict


def defval():
    return None


class Solution:
    def dfs(self, par, root, child):
        if not root:
            return

        if root.left:
            par[root.left.data] = root.data
            child[root.data].append(root.left.data)

            self.dfs(par, root.left, child)

        if root.right:
            par[root.right.data] = root.data
            child[root.data].append(root.right.data)
            self.dfs(par, root.right, child)

    def sum_at_distK(self, root, target, k):
        par = defaultdict(defval)
        child = defaultdict(list)

        self.dfs(par, root, child)
        q = [target]
        sumx = 0
        d = 0

        res = set()
        l = 1

        while len(q) > 0 and d <= k:
            curr = q.pop(0)
            l -= 1
            res.add(curr)
            sumx += curr
            if par[curr] and par[curr] not in res:
                q.append(par[curr])

            for i in child[curr]:
                if i not in res:
                    q.append(i)

            if l == 0:
                l = len(q)
                d += 1

        return sumx


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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input()
        root = buildTree(line)
        line = input().strip().split()
        target = int(line[0])
        k = int(line[1])
        obj = Solution()
        print(obj.sum_at_distK(root, target, k))
