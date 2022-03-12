#Input Description: A single line contains integers separated by space
#Output Description: Print the integer list of integers separated by space

#Sample Input : 2 3 4 5 6 7 8
#Sample Output : 2 3 4 5 6 7 8

# SOLUTION 1
userInput = list(map(int,input().split()))
print(*userInput)

# SOLUTION 2
# userInput = [int(x) for x in input().split()]
# print(*userInput)
