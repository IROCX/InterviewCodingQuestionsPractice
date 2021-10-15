# middle element of a singly linked list
# Day 13/100

# logic function
def findMid(head):
        count = 0
        temp = head
        if temp:
            while temp:
                count+=1
                temp = temp.next
        else:
            return -1

        
        target = (count//2) +1
        temp = head
        count = 0
        
        while temp:
            count +=1
            if count == target:
                target = temp.data
                break
            temp = temp.next
        
        return target


# Driver code

# Node class
class node:
    def __init__(self):
        self.data = None
        self.next = None


# linked list print function
def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Linked list class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        print(findMid(list1.head))
