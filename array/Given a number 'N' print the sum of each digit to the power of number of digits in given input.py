#Given a number 'N' print the sum of each digit to the power of number of digits in given input.
# Sample Testcase :
# INPUT
# 1234
# OUTPUT
# 354
'''
SOLUTION:
'''
n = int(input())
s = str(n)
lenDigit = len(s)
sumVal = 0
while(n):
    rem = n%10
    sumVal += rem**lenDigit
    n = n//10   
print(sumVal)
