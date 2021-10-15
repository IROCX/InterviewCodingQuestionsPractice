# check how many time string A needs to be repeated to make string B a substring of A, if not possible print -1
# Day 8/100

A = input()
B = input()

count = 0
temp = ""
if B in A:
    print(1)
else:
    while len(B)>len(temp):
        temp+=A
        count+=1
    if B in temp:
        print(count)
    else:
        if B in temp+A:
            print(count+1) 
        else:
            print(-1)