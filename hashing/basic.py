# This code checks how many times a number appears in an array using a simple counting method.
def check(arr, n, x):
    temp = [0 for i in range(n+1)]
    for i in arr:
        temp[i] += 1
    ans = temp[x]
    return ans

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,5 ,5]
n = len(arr)
x = 5
# result = check(arr, n, 111)
# print(f"The number {x} appears {result} times in the array.")

def char_str(s, x):
    temp = [0 for i in range(27)]
    for i in s:
        if i == ' ':
            continue
        temp[ord(i) - 97] += 1
    ans = temp[ord(x) - 97]
    return ans

s = "hello world"
x = 'l'
ans = char_str(s, x)
print(f"The character '{x}' appears {ans} times in the string '{s}'.")