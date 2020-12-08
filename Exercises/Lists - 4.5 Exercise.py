#Conner Zhao 12/05/20

# The reason why using a list reduces complexity is because instead of using many variable to define each name, you can do it by simpkly by adding all the names into a list. If every name and number are defined in individual variables, it would be a lot more complex for the programmer because when they are printing something they'll have do prin() for every single one of the variables.

"""
Create a new program in Repl.it called "Lists." Your goal for this program is to create sections of code that will perform different outputs with the list called, names which contains the following values - Peter, Bruce, Steve, Tony, Natasha, Clint, Wanda, Hope, Danny, Carol and the list called numbers which contains the following values - 100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80. At the beginning of your program, add in any comments and create the two lists. Then create the following:

A loop that will output every other name in the names list.
A loop that will output only the positive numbers in the numbers list.
A loop that will output the sum of all the values in the numbers list.
A loop that will output only the numbers that are odd.
A loop that will output only the names that come before "Thor" in the alphabet from the names list.
A loop that will  find the maximum or minimum value in the numbers list. This algorithm requires an additional variable that is assigned to the first element in the list. Then, in a loop compare each element to the variable. If the element is > (for max) or < (for min), assign the variable to the element. After the loop, print the variable.
HINT: len() is a helpful method that can be used on strings or lists to determine how "long" they are. For lists, that would mean how many elements are inside and for strings, that would mean how many characters long it is.
"""
names, numbers = ["Peter" , "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"], [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]
# A loop that will output every other name in the names list.
for name in names[::2]:
    print(name)
# A loop that will output only the positive numbers in the numbers list.
for num in numbers:
    if num >= 0:
        print(num)
# A loop that will output the sum of all the values in the numbers list.
print(sum(numbers))
# A loop that will output only the numbers that are odd.
for num in numbers:
    if num %2 != 0:
        print(num)
# A loop that will output only the names that come before "Thor" in the alphabet from the names list.
names.append("Thor")
# A loop that will find the maximum or minimum value in the numbers list. This algorithm requires an additional variable that is assigned to the first element in the list. Then, in a loop compare each element to the variable. If the element is > (for max) or < (for min), assign the variable to the element. After the loop, print the variable.
print(max(numbers))
print(min(numbers))