# Selection Sort Implementation
class Solution:
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            minn = i
            for j in range(i+1, n):
                if arr[minn] > arr[j]:
                    minn = j
            arr[minn], arr[i] = arr[i], arr[minn]
        return arr
    
# Bubble Sort Implementation
class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        swap = False
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = True
            if swap == False:
                return arr
        return arr
    
# Insertion Sort Implementation    
class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n):
            j = i
            while(j > 0 and arr[j] < arr[j - 1]):
                arr[j], arr[j-1] = arr[j-1],arr[j]
                j -= 1
        return arr
    
# Merge Sort Implementation
class Solution:
    def mergeSort(self, arr):
        low = 0
        n = len(arr)
        high = n-1
        def merging(arr, low, mid, high):
            temp = []
            i = low 
            j = mid + 1
            while(i <= mid and j <= high):
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while(i <= mid):
                temp.append(arr[i])
                i += 1
            while(j <= high):
                temp.append(arr[j])
                j += 1
            for i in range(len(temp)):
                arr[low + i] = temp[i]
            

        def merge(arr,low, high):
            if low >= high:
                return 
            mid = (low + high)//2
            merge(arr, low, mid)
            merge(arr, mid+1, high)
            merging(arr, low, mid, high)
        
        merge(arr, low, high)
        return arr

#quick sort implementation
class Solution:
    def quickSort(self, arr):
        n = len(arr)
        low = 0
        high = n-1
        def partition(arr, low, high):
            pivot = arr[low]
            i = low
            j = high
            while( i < j):
                while(arr[i] <= pivot and i <= high - 1):
                    i += 1
                while(arr[j] > pivot and j >= low + 1):
                    j -= 1
                if (i<j):
                    arr[i], arr[j] = arr[j], arr[i]
            arr[low], arr[j] = arr[j], arr[low]
            return j
        def quick(arr, low, high):
            if low < high: 
                pIndex = partition(arr, low, high)
                quick(arr, low, pIndex-1)
                quick(arr, pIndex+1, high)
        quick(arr, low, high)
        return arr

#largest element in an array
class Solution:
    def largestElement(self, arr):
        largest = arr[0]
        n = len(arr)
        for i in range(1,n):
            if arr[i] > largest:
                largest = arr[i]
        return largest
    
#smallest element in an array
class Solution:
    def secondLargestElement(self, arr):
        largest = -1
        second_largest = -1
        n = len(arr)
        for i in range(n):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            if arr[i] < largest and arr[i] > second_largest:
                second_largest = arr[i]
        return second_largest

# check array is sorted or not
class Solution:
    def isSorted(self, arr):
        #your code goes here
        isssorted = True
        n = len(arr)
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                isssorted = False
                return isssorted
        return isssorted

# Rotate an array by one position
class Solution:
    def rotateArrayByOne(self, arr):
        n = len(arr)
        low = arr[0]
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = low
        return arr

# Rotate an array by k positions
class Solution:
    def rotateArray(self, arr, k):
        temp = []
        n = len(arr)
        k = k%n
        for i in range(k):
            temp.append(arr[i])
        for i in range(k,n):
            arr[i-k] = arr[i]
        for i in range(k):
            arr[n-k+i] = temp[i]
        return arr

# Move all zeroes to the end of the array
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
    
 # Linear Search ImplementationS   
class Solution:
    def linearSearch(self, arr, x):
        ans = -1
        n = len(arr)
        for i in range(n):
            if arr[i] == x:
                ans = i
                return ans
        return ans 

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

# Find two indices such that the sum of the elements at those indices equals k
class Solution:
    def twoSum(self, arr, k):
        dic = {}
        n = len(arr)
        for i in range(n):
            elem = k - arr[i]
            if elem in dic:
                return [dic[elem], i]
            else:
                dic[elem] = i
        return [-1,-1]

# Sort Colors (Dutch National Flag Problem)
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        n = len(nums)
        for i in (nums):
            if i == 0:
                count0 += 1
            elif i == 1:
                count1 += 1
            elif i == 2:
                count2 += 2
        
        for i in range(0, count0):
            nums[i] = 0
        for i in range(count0, count0+count1):
            nums[i] = 1
        for i in range(count0 + count1, n):
            nums[i] = 2

# Find the majority element in an array (element that appears more than n/2 times)
class Solution:
    def majorityElement(self, nums):
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1 
            if dic[nums[i]] > n//2:
                return nums[i]   
# Second approach in more optimised way using Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, arr) -> int:
        n = len(arr)
        elem = None
        count = 0
        for i in arr:
            if count == 0:
                count = 1
                elem = i
            elif i == elem:
                count += 1
            else:
                count -= 1
        ans = 0
        for i in arr:
            if i == elem:
                ans += 1
        if ans > n//2:
            return elem 
        return -1

# Find the maximum subarray sum using Kadane's Algorithm
def max_sub(arr):
    n = len(arr)
    maxx = arr[0]
    summ = 0
    j = 0
    sub_arr = [0,0]
    for i in range(n):
        if summ == 0:
            j = i
        summ += arr[i]
        if summ > maxx:
            sub_arr[0] = j
            sub_arr[1] = i
            maxx = summ
        if summ < 0:
            summ = 0
    for i in range(sub_arr[0], sub_arr[1]+1):
        print(arr[i], end=" ")
    return maxx

# Rearrange an array such that positive and negative numbers are in alternate positions
class Solution:
    def rearrangeArray(self, arr):
        i = 0
        j = 1
        n = len(arr)
        temp = [0 for _ in range(n)]
        for k in range(n):
            if arr[k] > 0:
                temp[i] = arr[k]
                i += 2
            if arr[k] < 0:
                temp[j] = arr[k]
                j += 2
        return temp