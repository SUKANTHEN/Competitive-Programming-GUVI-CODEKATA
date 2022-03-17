#Given two numbers L,R print the smallest number which is divisible by both L and R.
#Sample Testcase :
#INPUT
#10 130
#OUTPUT
#130
'''
SOLUTION:
'''
def GCD(a,b):
    if a == 0:
        return b
    else:
        return GCD(b%a,a)
    
def LCM(a,b):
    return int((a*b)/GCD(a,b))
    
l,r = map(int,input().split())
res = LCM(l,r)
print(res)
