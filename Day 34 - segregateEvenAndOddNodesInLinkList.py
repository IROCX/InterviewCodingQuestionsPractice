# Given a link list of size N, modify it so that even numbers appear before all the odd numbers.
# The order of appearance of numbers within each segregation should be same as that in the original list.
# without creating new linked list

# Day 34/100


def divide(head):
    temp = head
    pre = None
    preoddflag = None
    oddflag = None

    while temp:
        if temp.data & 1 and oddflag == None:
            oddflag = temp
            preoddflag = pre
            pre = temp
            temp = temp.next
        elif temp.data & 1 == 0:
            if oddflag == None:
                pre = temp
                temp = temp.next
            else:
                pre.next = temp.next
                temp.next = oddflag
                if oddflag == head:
                    head = temp
                else:
                    preoddflag.next = temp
                preoddflag = temp
                temp = pre.next
        else:
            pre = temp
            temp = temp.next
    return head


#  Driver Code Starts

# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
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


def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print("")


# Driver Program
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        newhead = divide(list1.head)
        printlist(newhead)
