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
    
#  second largest element in an array   
class Solution:
    def secondLargestElement(self, arr):
        if not arr or len(arr) < 2:
            return -1 
        largest = second = -1
        for i in arr:
            if i > largest: 
                second = largest
                largest = i 
            elif i > second and i!= largest:
                second = i
        return second


# check if an array is sorted
class Solution:
    def isSorted(self, arr):
        flag = True
        n = len(arr)
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = False
                break
        return flag

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

# rotate an array by one position to the right
class Solution:
    def rotateArrayByOne(self, arr):
        n = len(arr)
        temp = arr[0]
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = temp
        return arr
    
# rotate an array by k positions to the right
class Solution:
    def rotateArray(self, arr, k):
        n = len(arr)
        k = k%n
        temp = []
        for i in range(k):
            temp.append(arr[i])
        temp1 = []                                                                    
        for i in range(k,n):
            temp1.append(arr[i])                                                        
        arr = [*temp1, *temp]
        return arr
    
# move all zeroes to the end of the array
class Solution:
    def moveZeroes(self, arr):
        n = len(arr)
        temp1 = []
        for i in arr:
            if i != 0:
                temp1.append(i)
        for i in range(len(temp1)):
            arr[i] = temp1[i]
        for i in range(len(temp1), n):
            arr[i] = 0
        return arr