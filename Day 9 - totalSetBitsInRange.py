# count number of set bits from 1 to n
# Day 9/100
import math

def countBits(n):
        x = math.log2(n)
        # print(x)
        
        if x == int(x):
            # print(111111, (2**(int(x)-1))*int(x))
            return int(2**(int(x)-1))*int(x) + n-(2**int(x))+1
        else:
            # print(222222, 2**(int(x)-1)*int(x), n-(2**int(x))+1)
            return 2**(int(x)-1)*int(x) + n-(2**int(x))+1 + countBits(n-(2**int(x)))
    
if __name__=='__main__':
    n = int(input())
    count = countBits(n)
    print(count)
