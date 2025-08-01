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