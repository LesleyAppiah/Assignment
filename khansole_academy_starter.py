"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
""
Khan
Academy is a
program
that
helps
users
to
add
by
asking
users
to
input
answers
for the addition of two randomly generated integers between 10 and 90 inclusive.The program returns feedback based on the answers of the user.""
import random

count1 = 1
while count1 <= 3:
    x = random.randint(10, 99)
if """This while function loops the following code repeatedly until the condition is met. Meaning it asks the user the addition of random numbers until the answer is provided for 3 consecutive times

# This code tells the computer to produce random numbers between 1 and 99.It is assigned a variable name,x.

    y=random.randint(10,99)

# This code tells the computer to produce random numbers between 1 and 99.It is assigned a variable name,y.
    R=x+y
#This code tells the computer to add x and y. It is given the variable,R.
    print("what is", x ,"+", y)
#This prints out what is x(random number from x) + y(random number from y)
    A=int(input("Answer:")
#The int function converts a string into an integer.

    if A==R:
    print("Congrats!",count1,"in a row.")
    count1*=1
#The "if" is a condition that if the user's answer "A" is equal to R, the users answer is right.
#count1*=1 is the defining index variable set at 1.

    else:
    print("Incorrect. The right answer is",R)
    count1=1
 #Else condition is there to print that the users answer is incorrect.

    print("Congratulation! You are now a master of additions")
 #This prints the "congratulations" after the user gets three correct answers in a row.
