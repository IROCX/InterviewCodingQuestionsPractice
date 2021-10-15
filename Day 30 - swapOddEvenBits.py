# for a given number, swap all even place bits by odd place bits - O(1)
# Day 30/100


def swapBits(n):
    return (n & 0xAAAAAAAA) >> 1 | (n & 0x55555555) << 1


#  Driver Code Starts
def main():

    T = int(input())

    while T > 0:

        n = int(input())
        print(swapBits(n))
        T -= 1


if __name__ == "__main__":
    main()
