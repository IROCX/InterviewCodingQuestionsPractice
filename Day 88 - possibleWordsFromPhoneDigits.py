# Day 88 / 100
# Given a nine digit mobile keypad and an N digit number which is represented by array
# List all words which are possible by pressing these numbers


def dfs(arr, res, word, ind, l):

    if arr == []:
        res.append(word)
        return

    for i in range(len(arr[0])):
        dfs(arr[ind:], res, word + arr[0][i], ind, l)


def possibleWords(a, N):
    d = {
        1: [],
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    chars = []
    for i in range(N):
        chars.append(d[a[i]])
    ind = 0
    res = []
    word = ""
    l = len(chars)
    dfs(chars[ind:], res, word, ind + 1, l)

    return res


#  Driver Code Starts
def main():

    T = int(input())

    while T > 0:

        N = int(input())
        a = [int(x) for x in input().strip().split()]
        res = possibleWords(a, N)
        for i in range(len(res)):
            print(res[i], end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
