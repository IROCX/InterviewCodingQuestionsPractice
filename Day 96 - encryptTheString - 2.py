# Given a string S
# Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of the number of occurrences of that letter
# Then the string thus obtained is further encrypted by reversing it
# Day 96 / 100


def encryptString(S):
    i = 1
    res = []
    count = 1

    while i < len(S):

        if S[i] == S[i - 1]:
            count += 1
        else:

            res.append(S[i - 1])
            res.append(hex(count)[2:])
            count = 1
        i += 1

    res.append(S[i - 1])
    res.append(hex(count)[2:])
    return "".join(res[::-1])


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        S = input()

        print(encryptString(S))
# } Driver Code Ends
