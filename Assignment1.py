# 1) The radius of a circle is 5.5. Write a script to compute the area of a circle.

pi = 3.14
radius = float(input('Please enter the radius of the circle:\n'))
area = pi * (radius*radius)
print('Thank You.','The area of the circle is',area,'.')

# 2) Write a program where python prints your name, then print them in reverse order with a comma between them. Put this in
#    the same cell: \n'

first_name = input('Please state your first name:\n')
last_name = input('Please state your last name:\n')
print(first_name+' '+last_name)
print('Hello',last_name,',',first_name,'.')

# 3) Write a program to test if a number is divisible by 5.

print('The program will check if the number entered is divisible by 5.')
value = int(input('Please enter a number:\n'))
if value % 5 == 0:  # if there is not a remainder, then the value is True and is divisible by 5 ( reason for '==' ).
    print(True)
if value % 5 != 0:  # if there is a remainder, then the value is False and is not divisible by 5 ( reason for '!=' ). 
    print(False)

# 4) What is the output of the following program?

a = 1
b = a * 2
c = 2 * b + 1

print(a,b,c)    # 1,2,5

# 5) What is the output of the following program?

a = 2
b = a * 2
c = b ** a
a = c % 2
print (a,b,c)   # 0,4,16

# 6) What is the output of the following program?

a = 5
b = a // 2
c = a / 2
a = a % 2
print (a,b,c)   # 1,2,2.5

# 7) Type each of the following commands and note each response.

print('Hello, World!')
print('Hello' 'World!')
print(3)
print(3.0)
print(2+3)
print(2.0+3.0)
print(2*3)
print(2**3)
print(7/3)
print(7//3)

# 8) Create a program with name and age. Have it print out a message addressed to name that tells them the year they will
#    turn 100 years old.

name = input('Please state your name:\n')
age = int(input('Please state your age:\n'))
import datetime
present = datetime.datetime.now()
difference = 100 - int(age)
print('Dear',name,',','you are now',age,'.','In the year',present.year + difference,'you will be 100 years old','.')

# 9) Create a sequence of numbers from 3 to 19 with increments of 2.

for x in range(3,21,2):
    print(x)

# 10) Try to solve this problem on your own first, then check your results with python.

a = 21
b = 10
c = 0
c = a + b
print('Line 1 - Value of c is',c)
c += a
print('Line 2 - Value of c is',c)
c *= a
print('Line 3 - Value of c is',c)
c /= a
print('Line 4 - Value of c is',c)
c  = 2
c %= a
print('Line 5 - Value of c is',c)
c **= a
print('Line 6 - Value of c is',c)
c //= a
print('Line 7 - Value of c is',c)
