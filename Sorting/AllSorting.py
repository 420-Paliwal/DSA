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