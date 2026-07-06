#Q1 Print numbers from 1 to 10.
print("numbers from 1 to 10")
for i in range(1,11):
    print (i)


# Q2 Print even numbers from 1 to 20.
print(" even numbers from 1 to 20")
for i in range (1,21,1):
    print (i)

# Q3 Print odd numbers from 1 to 20.
print("odd numbers from 1 to 20")
for i in range (1,21,2):    
    print (i)

# Q4 Find the sum of numbers from 1 to 100.
print(100*(100+1)/2)

# Q5 Print the multiplication table of a number.
for i in range(11):
    print("6X",i,"=",6*i)

# Q6 Reverse a number.
print("251"[::-1]) 

# Q7 Count the digits in a number.
print(len("784"))

# Q8 Check whether a number is a palindrome.
print("it's palindrome" if "100"[::-1]=="110" else "it's not a palindrome")

#Q9 Keep asking the user for input until they enter 0.
while True:
    number=input("Enter your number:")
    if number=="0":
        break

# Q10 Create a function to print "Hello".
def word(a):
    print(a)
word("hello")
  
# Q11 Create a function to add two numbers.
def addition (a,b):
    print(a+b)
addition(4,9)

# Q12 Create a function to check whether a number is even.
def even(e):
    if e%2==0:
        print("even number")
    else:
        print("odd number")
even(8)
# Q13 Create a function to find the maximum of two numbers.
print(max([1,4,89,79,509]))

# Q14 Create a function to find the factorial.
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(75)
# Q15 Create Shape with Circle and Rectangle. 
class Shape:
    def __init__(self,sides):
        self.sides=sides
circle=Shape(0)
rectangle=Shape(4)


