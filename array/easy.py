# remove duplicate elements from an array

class Solution:
    def removeDuplicates(self, arr):
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return len(dic)
    
