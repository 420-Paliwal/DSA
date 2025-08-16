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
    
# Union of two arrays
class Solution:
    def unionArray(self, nums1, nums2):
        dic = set(nums1)
        for i in nums2:
            if i not in dic:
                dic.add(i)
        return list(dic)      

# Find the missing number in an array of n elements
class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        summ = (n*(n+1))//2
        arr_summ = 0
        for i in arr:
            arr_summ += i 
        return summ - arr_summ 
    
# Find the maximum number of consecutive 1's in a binary array    
class Solution:
    def findMaxConsecutiveOnes(self, arr):
        maxx = 0
        i = 0
        n = len(arr)
        for j in range(n):
            if arr[j] == 1:
                i += 1
                if i > maxx:
                    maxx = i
            else:
                i = 0
        return maxx
            
# Find the single number in an array where every other number appears twice
class Solution:
    def singleNumber(self, nums):
        #your code goes here
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            if dic[i] == 1:
                return i 

#find the length of the longest subarray with sum equal to k
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        i = 0
        maxlen = 0
        summ = 0
        for j in range(n):
            summ += arr[j]
            while ( summ > k):
                summ -= arr[i]
                i += 1
            
            if (summ == k and j-i+1 > maxlen):
                maxlen = j-i+1
            
        return maxlen