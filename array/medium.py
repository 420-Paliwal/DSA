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
    
# Find the length of the longest consecutive sequence in an unsorted array
class Solution:
    def longestConsecutive(self, arr) -> int:
        arr = set(arr)
        n = len(arr)
        if n < 1:
            return n
        large = 0
        for x in arr:
            if (x-1 not in arr):
                count = 1
                while(x+1 in arr):
                    x += 1
                    count += 1
                if count > large:
                    large = count
        return large
    
# Set Matrix Zeroes
class Solution:
    def setZeroes(self, arr) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(arr)
        cols = len(arr[0])
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    for k in range(cols):
                        if arr[i][k] != 0:
                            arr[i][k] = None
                    for l in range(rows):
                        if arr[l][j] != 0:
                            arr[l][j] = None
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == None:
                    arr[i][j] = 0
        return arr

# Rotate a matrix by 90 degrees clockwise
class Solution:
    def rotate(self, arr) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(arr)
        n = row
        col = len(arr[0])
        temp = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                temp[j][n-1-i] = arr[i][j]
        for i in range(row):
            for j in range(col):
                arr[i][j] = temp[i][j]