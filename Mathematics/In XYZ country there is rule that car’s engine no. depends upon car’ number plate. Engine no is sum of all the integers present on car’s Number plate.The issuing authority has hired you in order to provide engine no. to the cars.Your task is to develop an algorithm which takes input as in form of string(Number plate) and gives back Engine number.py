# Q) In XYZ country there is rule that car’s engine no. depends upon car’ number plate. Engine no is sum of all the integers present on car’s Number plate.The issuing authority has hired you in order to provide engine no. to the cars.Your task is to develop an algorithm which takes input as in form of string(Number plate) and gives back Engine number
# Sample Input :
# HR05-AA-2669
# Sample Output :
# 28
"""
SOLUTION:
"""
def engineNumCalculator(s):
    summer = 0
    for i in s:
        if i.isdigit() == True:
            summer += int(i)
    return summer
    
s = input()
val = engineNumCalculator(s)
print(val)
