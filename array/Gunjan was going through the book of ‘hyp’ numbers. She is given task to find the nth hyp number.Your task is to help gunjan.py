# Gunjan was going through the book of ‘hyp’ numbers. She is given task to find the nth hyp number.Your task is to help gunjan
#A hyp number is a number whose all digits are prime.
# Sample Input :
# 3
# Sample Output :
# 5
'''
SOLUTION:
'''
''' Credicts from Geek for Geeks https://www.geeksforgeeks.org/finding-n-th-number-made-prime-digits/  '''

def nthPrimeNumber(n):
  num = ""
  while(n>0):
    rem=n%4
    if(rem==1):
      num += '2'
    if rem==2:
      num += '3'
    if rem==3:
      num+= '5'
    if rem==0:
      num+= '7'
    if (n%4) == 0:
      n = n-1
    n = n//4
  return num[::-1]

num = int(input())
val = nthPrimeNumber(num)
print(val)
