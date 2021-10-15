# count all occurrences of anagrams of given string in other string
# Day 12/100

txt = input()
pat = input()

l1 = len(txt)
l2 = len(pat)

d = {}
f = {}
count = 0

c = 97
for i in range(26):
    d[chr(c+i)]=0
    f[chr(c+i)]=0

if l1<l2:
    print(0)
if l1 == l2:
    if pat == txt:
        print(1)
    else:
        print(0)

for i in range(l2):
    f[txt[i]]+=1
    
for i in pat:
    d[i]+=1

if d == f:
    count+=1

for i in range(1,l1-l2+1):
    
    f[txt[i-1]]-=1
    f[txt[i+l2-1]]+=1
    
    # print(f)
    
    if f == d:
        count+=1
print(count)