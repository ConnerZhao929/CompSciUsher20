#Conner Zhao 12/05/20
import random
"""
Add the beginning comments at the top of the program.
In the first part of your program, create a for loop that runs three times:
	Inside the for loop, prompt the user for an integer
	Prompt the user for another integer
	Call the function compare (you are going to create this function next)
	Pass the variables that you used for the integer inputs from above
Create a function called compare (remember the function definition should go at the top of the program) and use two variables in the parameters of the function:
	Inside of the function, create an if / elif / else structure that compares the two values passed into the function
	If one value is less than the other, output that to the user (Ex: 2 is less than 4)
	Elif the other value is less than the other output something similar (Ex: 4 is less than 9)
	Else, output that they are equal to each other
That is it for the first part of the program.
Next, create an empty list called names.
Create a loop that runs 6 times:
	Inside of the for loop, prompt the user for a name
	Append the name to the list
Outside of the for loop, prompt the user for how many people they would like to vote off the island.
Call the function eliminate and pass the variable you used from step 7 to it.
Also, this function will return a value, so store this back function call back to a new variable.
Create a function called eliminate and create a variable to use as the parameter:
	Inside the function, randomly shuffle (use the shuffle() method) all the values in the list (you will need to import random at the top of the program)
	Then using a for loop, loop it as many times as the value that was passed to the function:
		Inside the for loop, remove one name from the list (use the pop() method)
	Outside the for loop, but still inside the function, return the list of remaining people
Underneath where you left off in step 8, print the remaining people that are left: those that did not get voted off the island.
"""	
def compare(num1, num2):
	if num1>num2:
		print(str(num1)+"is larger than " +str(num2))
	elif num2>num1:
		print(str(num2)+"is larger than " + str(num1))
	else:
		print(str(1) +'is equal to '+str(num2))

def eliminate(number):
	random.shuffle(names)
	for i in range(number):
		names.pop()
		return names;

for i in range(3):
	n1 = int(input('Enter an nterger: '))
	n2 = int(input('Enter another interger: '))
	compare(n1,n2)
print('\n\n')

names = []
for i in range(6):
	person= input('Enter a name: ')
	names.append(person)

elim = int(input('How many people do you want to kick off the island? '))
newNames = eliminate(elim)
print('These are the people left: '+str(newNames))