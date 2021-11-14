# Given a string, count number of reversals of { to } or vice versa to make string valid and balanced expression
# Day 61/100

def countRev(s):
    # your code here
    st = []
    count = 0

    if len(s) & 1:
        return -1

    for i in s:
        if i in "{":
            st.append(i)
        else:
            if len(st) == 0:
                st.append("{")
                count += 1
            else:
                st.pop()
    l = len(st)
    count += l // 2
    return count


#  Driver Code Starts
t = int(input())
for tc in range(t):
    s = input()
    print(countRev(s))
