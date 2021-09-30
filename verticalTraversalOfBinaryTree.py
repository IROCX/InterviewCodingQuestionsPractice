# find the vertical traversal sequence of a binary tree - same vertical line elements must be considered in level-order
# Day 16/100

# input in form of perfect binary tree - 1 2 3 4 N N 6 (input "N" for absent nodes in the perfect binary tree)

from collections import defaultdict

def defvallist():
    return []
    
def defval():
    return defaultdict(defvallist)
    

def dfs(head, d, line, lev):
    
    if head == None:
        return
    else:
        d[line][lev].append(head.data)
        
        dfs(head.left, d, line-1, lev+1)
        dfs(head.right, d, line+1, lev+1)
        
        
#Function to find the vertical order traversal of Binary Tree.
def verticalOrder(root): 
    d = defaultdict(defval)
    
    dfs(root, d, 0, 0)

    res = []
    
    # print(dict(d))

    for i in sorted(d.keys()):
        for j in sorted(d[i].keys()):
            
        # print(res)
            res.extend(d[i][j])
        # print(res)
    return res

# Driver Code
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input()) 
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()