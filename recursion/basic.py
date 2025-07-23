# This is a simple recursive function to print numbers from 1 to n.
class Solution:
    def printNumbers(self, n):
        # Your code goes hee
        if (n <= 0):
          return 
        self.printNumbers(n-1)
        print(n)

