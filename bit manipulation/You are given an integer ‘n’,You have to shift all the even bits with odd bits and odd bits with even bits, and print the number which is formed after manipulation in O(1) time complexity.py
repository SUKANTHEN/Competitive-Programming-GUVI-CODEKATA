# Q) You are given an integer ‘n’,You have to shift all the even bits with odd bits and odd bits with even bits, and print the number which is formed after manipulation in O(1) time complexity.
# Sample Input :
# 23
# Sample Output :
# 43
'''
SOLUTION:
'''
def SwapBits(n):
    evenBits = n & 0xAAAAAAAA
    oddBits = n & 0x55555555
    evenBits >>= 1
    oddBits <<= 1
    return (evenBits | oddBits)
    
n = int(input())
val = SwapBits(n)
print(val)
