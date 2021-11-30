# Given a BST, find the shortest range [x, y],
# such that at least one node of every level of the BST lies in the range.
# Day 76/100


import heapq


def shortestRange(root):

    q = [root]
    temp = 1
    lvl = 0
    trav = []

    while q != []:

        ele = q.pop(0)
        trav.append([])
        trav[lvl].append(ele.data)
        temp -= 1

        if ele.left:
            q.append(ele.left)
        if ele.right:
            q.append(ele.right)

        if temp == 0:
            temp = len(q)
            lvl += 1

    trav = [i for i in trav if i != []]

    pq = []
    n = len(trav)
    maxx = 0

    for i in range(n):
        heapq.heappush(pq, (trav[i][0], i, 0))
        maxx = max(maxx, trav[i][0])

    ans = [pq[0][0], maxx]

    while True:
        _, list_index, num_index = heapq.heappop(pq)
        if num_index == len(trav[list_index]) - 1:
            break

        next_num = trav[list_index][num_index + 1]
        maxx = max(maxx, next_num)
        heapq.heappush(pq, (next_num, list_index, num_index + 1))
        if (maxx - pq[0][0]) < (ans[1] - ans[0]):
            ans = [pq[0][0], maxx]

    return ans


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
    from collections import deque

    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ans = shortestRange(root)
        print(ans[0], ans[1])
