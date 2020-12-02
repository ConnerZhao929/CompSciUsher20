#Conner Zhao nov18th
userInput = int(input('Please pick a number from 1 to 100'))
while userInput <=1 or userInput >=100:
        print('That is an invalid number')
        userInput = int(input('Please pick a number from 1 to 100'))
        userInput = userInput
print('thank you for your input' + userInput)