# Conner Zhao nov18th
"""
Create a variable and assign it the value of 1
Prompt the user to guess your favorite color
While their guess is not equal to your favorite color
    Tell them they are incorrect
    Prompt them to guess again
    Add one to the variable above
Output to the user, they were correct and how many attempts it took using the variable
"""
Number = 1
Color = input('guess my favorite color: ')
favClr = "White"
Color = str(Color)
while Color != favClr:
    print("My favorite color is not " + Color + " please try again")
    Color = input('guess my favorite color')
    Number = Number + 1
print("Congrats! You guessed it! My favorite color is " + favClr)
Number = str(Number)
print("it took you " + Number + ' attempts')
