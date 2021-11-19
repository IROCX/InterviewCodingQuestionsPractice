# Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths
# Find the length of the shortest transformation sequence from startWord to targetWord.

def wordLadderLength(startWord, targetWord, wordList):

    alphas = [0] * 26
    for i in range(97, 97 + 26):
        alphas[i - 97] = chr(i)

    endWordPresent = 0
    for i in range(len(wordList)):
        if wordList[i] == targetWord:
            endWordPresent = 1

    if not endWordPresent:
        return 0

    q = [startWord]
    wordList = set(wordList)
    d = 1
    l = 1

    while len(q):

        curr = q.pop(0)
        l -= 1

        for i in range(len(curr)):
            currentChar = curr[i]
            for j in alphas:

                if j != currentChar:
                    curr = curr[:i] + j + curr[i + 1 :]
                    if curr == targetWord:
                        return d + 1
                    else:
                        if curr in wordList:
                            q.append(curr)
                            wordList.remove(curr)

            curr = curr[:i] + currentChar + curr[i + 1 :]
        if l == 0:
            d += 1
            l = len(q)

    return 0


#  Driver Code Starts
from collections import deque

if __name__ == "__main__":
    T = int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
      
        ans = wordLadderLength(startWord, targetWord, wordList)
        print(ans)

