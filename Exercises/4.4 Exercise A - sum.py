#Conner Zhao nov18th
"""
Create a variable and assign it the value of 0
Prompt the user for how many numbers they have
With a for loop, set it to repeat enough times to get all their values
    Prompt the user for a number
    Add that number to the variable that started as 0
Output to the user, the sum of all values
"""
sumNum = 0
amntNum = input("How many numbers do you want to add together?: ")
amntNum = int(amntNum)
for i in range(amntNum):
        numadded = input("Give me one of those numbers: ")
        numadded = int(numadded)
        sumNum = sumNum + numadded
print("The sum of your numbers is : " + str(sumNum))