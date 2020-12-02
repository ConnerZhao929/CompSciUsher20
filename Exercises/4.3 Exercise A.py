"""
1.   grade == 82
2.   grade >= 82 and grade + 10 < 100
3.   grade / 2 > 90 or grade == 75
4.   not(name != "Rumpelstiltskin")
5.   name == "Jim" or name == "Rumpelstiltskin"
6.   x + 3 > 0 or x != -3 or x - 1 < -5
7.   (x < 0 and x != 3) and x + 5 == 2
8.   grade > 65 and (name == "Michael" or name == "Rumpelstiltskin") and not(x == -3)
9.   x > 0 or (grade + 5 < 90 and grade >= 80) or name == "Pam"
10.  (not(grade > x) and (name != "Dwight" and x <= 0)) or (grade > 0 and x % 2 == 1)
"""
grade = 82
name = "Rumplestiltskin"
x = -3
print(grade == 82)
print(grade >= 82)
print(grade + 10 < 100)
print(grade / 2 > 90)
print(not(name != "Rumpelstiltskin"))
print(name == "Jim")
print(x + 3 > 0)
print(x < 0)
print(x != 3)
print(x + 5 == 2)
print(grade > 65)
print(name == "Michael")
print(not(x == -3))
print(x > 0)
print(grade + 5 < 90)
print(grade >= 80)
print(not(grade > x))
print(name != "Dwight")
print(x <= 0)



