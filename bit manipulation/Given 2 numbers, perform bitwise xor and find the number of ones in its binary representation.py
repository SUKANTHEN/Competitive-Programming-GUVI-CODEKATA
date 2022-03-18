# Q) Given 2 numbers, perform bitwise xor and find the number of ones in its binary representation.
# Sample Testcase :
# INPUT
# 10 5
# OUTPUT
# 4
'''
SOLUTION:
'''
def biwiseOnesCounter(num):
    val = 0
    n = str(bin(num))
    if "1" in n:
        val = n.count("1")
    return val

num1,num2 = map(int,input().split())
bitwiseXOR = num1 ^ num2
res =  biwiseOnesCounter(bitwiseXOR)
print(res)
