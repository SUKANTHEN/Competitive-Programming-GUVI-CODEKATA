#Sample Input :
# 4
# 2 4 6 8

#Sample Output : 24

'''
SOLUTION:
'''
def LCMCalculator(num1,num2):
    if(num1>num2):
        numerator = num1
        denominator = num2
    else:
        numerator = num2
        denominator = num1
    rem = numerator % denominator
    while (rem != 0):
        numerator = denominator
        denominator = rem
        rem = numerator % denominator
    gcd = denominator
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

n = int(input())
arr = [int(x) for x in input().split()]
if len(arr) == 1:
    print(*arr)
elif len(arr) == 2:
    arr = sorted(arr)
    num1 = arr[0]
    num2 = arr[1]
    lcm = LCMCalculator(num1, num2)
    print(lcm)
else:
    arr = sorted(arr)
    num1 = arr[0]
    num2 = arr[1]
    lcm = LCMCalculator(num1, num2)
    for i in range(2, len(arr)):
        lcm = LCMCalculator(lcm, arr[i])
    print(lcm)
