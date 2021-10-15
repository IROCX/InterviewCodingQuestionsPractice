# check if a given tree is BST with no equal nodes
# Day 17/100

# approach - inorder traversal of a BST gives increasing sequence of numbers
# input - 
    # 1st line - no of testcases
    # 2nd line - perfect binary tree sequence padded with "N" for absent nodes
    # eg - 
    # 1
    # 1 1 1 1 1 N 1 1 1 1 1
# output
    # return 1 if it is a valid binary tree  
    # return 0 otherwise


def inorderTraversal(root, inorderT):
    if root == None:
        return
    else:
       
        inorderTraversal(root.left, inorderT)
        inorderT.append(root.data)
        inorderTraversal(root.right, inorderT)
        

   
#Function to check whether a Binary Tree is BST or not.
def isBST( root):
    
    inorderT = []

    inorderTraversal(root, inorderT)
    
    res = 1
    for i in range(len(inorderT)-1):
        if inorderT[i]>=inorderT[i+1]:
            res = 0
            break
    
    return res




#  Driver Code
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
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if isBST(root):
            print(1) 
        else:
            print(0)