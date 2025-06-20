# largest element in an array
class Solution:
    def largestElement(self, arr):
        if not arr:
            return -1
        n = len(arr)
        if n < 2:
            return arr[0]
        maxx = arr[0]
        for i in arr:
            if i > maxx:
                maxx = i
        return maxx


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
    
