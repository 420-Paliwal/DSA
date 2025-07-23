# This is a simple recursive function to print numbers from 1 to n.
class Solution:
    def printNumbers(self, n):
        # Your code goes hee
        if (n <= 0):
          return 
        self.printNumbers(n-1)
        print(n)

# This is a simple recursive function to print numbers from n to 1.
class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if (n <= 0):
          return
        print(n)
        self.printNumbers(n-1)

# This is a simple recursive function to calculate the sum of first n natural numbers.
class Solution:
    def NnumbersSum(self, n):
        #your code goes here
        if (n <= 0):
            return 0
        return n + self.NnumbersSum(n-1)
    
# This is a simple recursive function to calculate the product of first n natural numbers.
class Solution:
    def Factorial(self, n):
        #your code goes here
        if (n <= 1):
            return 1
        return n * self.Factorial(n-1)
    
# This is a simple recursive function to reverse an array.
class Solution:
    def reverse(self, arr, n):
        low = 0 
        high = n-1
        def rev_arr(arr,low, high):
            if low >= high:
                return arr
            arr[low], arr[high] = arr[high], arr[low]
            rev_arr(arr, low + 1, high - 1)
        ans = rev_arr(arr, low, high)
        return ans