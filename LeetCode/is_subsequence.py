def isSubsequence(s, t):
    string = [x for x in s]
    subsequence = [x for x in t]
    j = 0
    for i in range(len(subsequence)):
        if string[j] == subsequence[i]:
            j = j + 1
        if j == len(string):
            return True
    return False


# test = isSubsequence('aec', 'abcde')
# test = isSubsequence(s = "abc", t = "ahbgdc")
test = isSubsequence(s = "axc", t = "ahbgdc")
print(test)
# ace
# a b c d e
