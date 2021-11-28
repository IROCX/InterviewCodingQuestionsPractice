# Given a sorted linked list of distinct nodes and an integer X
# Count distinct triplets in the list that sum up to given integer X
# Day 75/100
from collections import defaultdict


def defval():
    return 0


def countTriplets(head, x):

    tmp = defaultdict(defval)

    temp = head

    while temp:
        tmp[temp.val] += 1
        temp = temp.nxt

    count = 0
    temp = head
    temp2 = head
    while temp:
        temp2 = temp.nxt
        while temp2:
            diff = x - (temp.val + temp2.val)

            if diff != temp.val and diff != temp2.val and tmp[diff] != 0:
                count += 1

            temp2 = temp2.nxt
        temp = temp.nxt

    return count // 3


#  Driver Code Starts
class Node:
    def __init__(self, x):
        self.val = x
        self.nxt = None


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        x = int(line[1])
        line = input().strip().split()

        head = Node(int(line[0]))
        tail = head
        for i in range(1, n):
            tail.nxt = Node(int(line[i]))
            tail = tail.nxt

        print(countTriplets(head, x))
