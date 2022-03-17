# Q) Given a number N, print their prime factors in sorted order.
#Input Size : 2 <= N <= 100000
#Sample Testcase :
# INPUT
# 18
# OUTPUT
# 2 3
'''
SOLUTION:
'''
def primeFactors(n):
    ''' Using Sieve Of Eratosthenes'''
    prime_list = []
    lst  =[]
    for i in range(2, int(n)+1):
        if i not in prime_list and (n%i==0):
            lst.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return lst

n = int(input())
res = primeFactors(n)
print(*res)
