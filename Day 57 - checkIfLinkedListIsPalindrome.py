# Given a singly linked list of integers, check if the given linked list is palindrome or not
# Day 57/100

def isPalindrome(head):
    
    if not head:
        return 0
        
    temp = head
    length = 0
    while temp:
        length+=1
        temp = temp.next
        
    if length == 1:
        return 1
    
    temp = head
    counter = length//2
    while counter>0:
        temp = temp.next
        counter-=1
        
    if length&1:
        temp = temp.next
        
    temp2 = temp.next
    temp3 = None
    temp.next = None
  
    while temp2:
        temp3 = temp2.next
        temp2.next = temp
        temp = temp2
        temp2 = temp3
    head2 = temp
  
    while head and head2:
        if head.data != head2.data:
            return 0
        head = head.next
        head2 = head2.next
    return 1


#  Driver Code Starts

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if isPalindrome(a.head):
            print(1)
        else:
            print(0)