# Given a singly linked list and a number k
# Write a function to find the (N/k)th element, where N is the number of elements in the list
# Consider ceil value in case of decimals
# Day 90 / 100

from math import ceil


def fractionalNodes(head, k):

    l = 1
    temp = head
    while temp.next:
        l += 1
        temp = temp.next
    target = ceil(l / k)

    l = 1
    temp = head
    while l < target:
        temp = temp.next
        l += 1
    return temp


# Driver Code Starts
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self, node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        for i in range(0, len(arr)):
            lis.insert(arr[i])
        ans = fractionalNodes(lis.head, k)
        print(ans.data)
