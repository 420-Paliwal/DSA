# This is a simple function to check if a string is a palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        if n <= 1:
            return True
        low = 0 
        high = n-1
        while (low < high):
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True