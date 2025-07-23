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

