# Q) A person saves his monthly saving according to given schema. He saves same amount of money which is equal to the money saved in immediate previous two months. Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell how much he had totally saved at the end of ‘n’ months
# Sample Input :
# 1
# Sample Output :
# 2000
"""
SOLUTION:
"""
n = int(input())
initialAmt = 1000; month1savings = 1000
amountSavings = [initialAmt,month1savings]
if n == 1:
    val = sum(amountSavings)
else:
    for i in range(1,n):
        lastElem = amountSavings[len(amountSavings)-1]
        last2Elem = amountSavings[len(amountSavings)-2]
        savings = lastElem + last2Elem
        amountSavings.append(savings)
    val = sum(amountSavings)
print(val)
