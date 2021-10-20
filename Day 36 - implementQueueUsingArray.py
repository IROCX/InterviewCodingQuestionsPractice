# Implement Queue using array
# Day 36/100


class MyQueue:
    def __init__(self):
        self.q = []

    # Function to push an element x in a queue.
    def push(self, x):
        self.q.append(x)

    # Function to pop an element from queue and return that element.
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.q.pop(0)

    def isEmpty(self):
        return len(self.q) == 0


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while i < len(q1):
            if q1[i] == 1:
                s.push(q1[i + 1])
                i = i + 2
            elif q1[i] == 2:
                print(s.pop(), end=" ")
                i = i + 1
            elif s.isEmpty():
                print(-1)
                i = i + 1
        print()

