# This code checks how many times a number appears in an array using a simple counting method.
def check(arr, n, x):
    temp = [0 for i in range(n+1)]
    for i in arr:
        temp[i] += 1
    ans = temp[x]
    return ans

# This code checks how many times a character appears in a string using a simple counting method.
def char_str(s, x):
    temp = [0 for i in range(27)]
    for i in s:
        if i == ' ':
            continue
        temp[ord(i) - 97] += 1
    ans = temp[ord(x) - 97]
    return ans


# This code finds the most frequent element in an array using a dictionary to count occurrences.
class Solution:
    def mostFrequentElement(self, arr):
        mapp = {}
        for i in arr:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1
        max = 0
        val = 0
        for i in mapp:
            if mapp[i] > max:
                max = mapp[i]
                val = i
        return val