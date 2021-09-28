# sort stack
# Day 14/100

def stackSort(s):
    
    temps = []
    temparr = []
    while len(s)>0:
        e = s.pop(0)
        
        if temps == []:
            # print(1111, temps)
            temps.append(e)
        else:
            # print(22222, temps)
            if temps[-1]<=e:
                temps.append(e)
            else:
                while temps != [] and temps[-1] > e:
                    temparr.append(temps.pop())
                temps.append(e)
                while temparr != []:
                    temps.append(temparr.pop())
    # print(temps, s)
    while temps != []:
        s.append(temps.pop())


n = int(input())
arr = list(map(int, input().strip().split()))
stackSort(arr)
for e in range(len(arr)):
    print(arr.pop(0), end=" ")
