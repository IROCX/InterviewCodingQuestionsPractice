# Given an expression string x, check whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp
# Day 60/100

def ispar(x):
    st = []
    for i in x:
        if i in ["(", "{", "["]:
            st.append(i)
        elif i == "}":
            if len(st) != 0 and st[-1] == "{":
                st.pop()
            else:
                return False
        elif i == "]":
            if len(st) != 0 and st[-1] == "[":
                st.pop()
            else:
                return False
        elif i == ")":
            if len(st) != 0 and st[-1] == "(":
                st.pop()
            else:
                return False

    if len(st) == 0:
        return True
    else:
        return False


#  Driver Code Starts

if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
