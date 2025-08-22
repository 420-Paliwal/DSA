class Solution:
    def search(self, arr, x) -> int:
        low = 0
        high = len(arr)-1
        while(low <= high):
            mid = (low + high)// 2
            if arr[mid] > x:
                high = mid-1
            elif arr[mid] < x:
                low = mid+1
            elif arr[mid] == x:
                return mid
        return -1 
    
def lower_bound(arr, x):
    low = 0
    high = len(arr) - 1
    large = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            high = mid - 1
            large = mid
        elif arr[mid] < x:
            low = mid + 1
    return large

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
print(lower_bound(arr, x))  # Output: 4 (index of the first element

# greater than or equal to 5)
class Solution:
    def upperBound(self, arr, x):
        n = len(arr) 
        low = 0 
        high = n - 1
        small = -1
        while(low <= high):
            mid = (low + high )// 2
            if (arr[mid] <= x):
                low = mid + 1
            else:
                small = mid
                high = mid - 1
        if small == -1:
            return n 
        else:
            return small