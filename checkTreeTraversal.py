# check if given preorder, inorder & postorder traversals are of the same tree or not.
# Day 10/100

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(inorder, preorder):
    if len(inorder) == 0:
        return None, 1

    head = Node(preorder[0])
    if preorder[0] in inorder:
        ind = inorder.index(preorder[0])
    else:
        flag = -1
        return None, -1

    preorder.pop(0)
    head.left, flag = createTree(inorder[:ind], preorder)
    head.right, flag = createTree(inorder[ind + 1 :], preorder)

    return head, flag
    
def getPostorder(root, res):

    if root:

        getPostorder(root.left, res)

        getPostorder(root.right, res)

        return res.append(root.data)

if __name__ == '__main__':
    print(__name__)

    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    head, flag = createTree(inorder, preorder)
    if flag == -1:
        print("No")
    else:
        res = []
        getPostorder(head, res)
        if res == postorder:
            print("Yes")
        else:
            print("No")