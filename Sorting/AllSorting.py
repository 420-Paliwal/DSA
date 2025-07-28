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
        swap = False
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = True
            if swap == False:
                return arr
        return arr