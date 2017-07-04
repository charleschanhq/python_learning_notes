from decimal import Decimal
import math
import random

'''

number=input("please enter a number: ")
print(type(number))
newnumber=int(number)
print(type(newnumber))


------------------------------------------------------------
'''
'''
#学习except
while True:
    try:
        number=int(input("please enter an number: "))
        break
    except ValueError:
        print(   "You did not enter a number")
    except:
        print(   "This is an unknown error")

print ("Thanks for entering a valid number!")
'''




'''
#猜数字游戏：1-10之间猜一个指定数字
secret_number=6
while True:
    guess_number=int(input("please enter a number from 1 to 10: "))
    if guess_number==secret_number:
        print("You guessed it!")
        break

'''

#math function ：
# ceil 向上取整 //  floor 向下取整 //fabs 绝对值

'''
newnumber1=Decimal(0)
newnumber=0.0000000000001
loopnumber=20
while loopnumber< 20:
    newnumber=newnumber+1
    loopnumber=loopnumber+1
print(newnumber)



print('hello' *10)
'''



# Unicode： A-Z 65-90      a-z 97-122
#输入一串string， 转换成unicode， 然后再转换成原来的string
'''
newstring=input("pleas enter an string: ")
hidestring=[]
for i in newstring:
    hidestring.append(str(ord(i)))
    print(hidestring)
print('the transfer process is done')
showingstring=''
for n in hidestring:
    showingstring=showingstring+str(chr(int(n)))
    print(showingstring)
'''




#string module
#a_list=["a","b"," abc"]
#print("".join(a_list))


#GET THE ABBR OF THE INPUT LIST
'''
newstring=input("please enter the string: ")
newstring=newstring.upper()
newlist=newstring.split()
for each_word in newlist:
    print(each_word[0],end="")
'''


'''
# Returns True if characters are letters or numbers
# Whitespace is false
letter_z="a"
num_3="1024.1024"
a_space=" "
print("Is z a letter or number :", letter_z.isalnum())
# Returns True if characters are letters
print("Is z a letter :", letter_z.isalpha())
# Returns True if characters are numbers (Floats are False)
print("Is 3 a number :", num_3.isdigit())
# Returns True if all are lowercase
print("Is z a lowercase :", letter_z.islower())
# Returns True if all are uppercase
print("Is z a uppercase :", letter_z.isupper())
# Returns True if all are spaces
print("Is space a space :", a_space.isspace())
'''


'''
# check if a number if a prime number
def isprime(num):

    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def getPrimes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        if isprime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)

'''



#--------------------------------------------------------------------------------------------------------------------
# get the area for what shape
'''
def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape =="circle":
        circle_area()
    else:
        print("Please enter circle or rectangle")

def rectangle_area():
    length = input("please enter the length of the rectangle")
    length= float(input)
    width=input("please enter the width of the rectangle")
    width=float(width)
    area=length*width
    print("the area of the rectangle is: ",area)


def circle_area():
    radius = float(input("Enter the radius : "))
    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is {:.2f}".format(area))
'''

'''
list1=['string',1,222]
onetotenlist = list(range(10))
#print (onetotenlist)
onetotenlist=list1+onetotenlist
#print( onetotenlist)
index_of_one= onetotenlist.index(222)
#print(index_of_one)
#print(onetotenlist.count(1))
onetotenlist.append(1)
#print(onetotenlist)


# bubble sorting
numList=[3,2,1,4,53,2,1]
i = len(numList) - 1
while i > 1:
    j = 0
    while j < i:
        # Tracks the comparison of index values
        print("\nIs {} > {}".format(numList[j], numList[j + 1]))
        print()
        # If the value on the left is bigger switch values
        if numList[j] > numList[j + 1]:
            print("Switch")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")
        j += 1
        # Track changes to the list
        for k in numList:
            print(k, end=", ")
        print()
    print("END OF ROUND")
    i -= 1
for k in numList:
    print(k, end=", ")
print()

# ---------- PROBLEM : CREATE MULTIPLICATION TABLE ----------
# With 2 for loops fill the cells in a multidimensional
# list with a multiplication table using values 1 - 9
'''
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
4, 8, 12, 16, 20, 24, 28, 32, 36,
5, 10, 15, 20, 25, 30, 35, 40, 45,
6, 12, 18, 24, 30, 36, 42, 48, 54,
7, 14, 21, 28, 35, 42, 49, 56, 63,
8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81
'''
# Create the multidimensional list
multTable = [[0] * 10 for i in range(10)]
# This will increment for each row
for i in range(1, 10):
    # This will increment for each item in the row
    for j in range(1, 10):
        # Assign the value to the cell
        multTable[i][j] = i * j
# Output the data in the same way you assigned it
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=", ")
    print()
    
'''

#new bubble sorting    wrong sample
'''
listone=[2,3,4,5,1,7,8,10]
newlist=listone
sortedlist=[]
length=len(newlist)
for i in range(0,length):
    for j in newlist:
        if newlist[i]<=newlist[j]:
            temp=newlist[i]
        sortedlist.append(newlist[i])
        newlist.remove(newlist[i])
        length=len(newlist)
print(sortedlist)
'''
'''

# let me do the bubble sorting again  , correct version
listone=[5,4,2,6,8,5,3,2,6,9,10,12,13,4,2,2,3]
listlen=len(listone)
loop=0
while loop<listlen:
    for i in range(0,listlen-1):
        if listone[i]>=listone[i+1]:
            temp1=listone[i]
            listone[i]=listone[i+1]
            listone[i+1]=temp1
    print(listone,"sort time:",loop+1)
    loop=loop+1
# yeah! I did it!


'''

'''

#function
# ---------- UNKNOWN NUMBER OF ARGUMENTS ----------
# We can receive an unknown number of arguments using
# the splat (*) operator

def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


print("Sum :", sumAll(1, 2, 3, 4))

# ---------- pythontut2.py ----------

# We need this module for our program
import math


# Functions allow us to avoid duplicate code in our programs

# Aside from having to type code twice duplicate code is bad
# because it requires us to change multiple blocks of code
# if we need to make a change

# ---------- OUR FUNCTIONS ----------

# This routes to the correct area function
# The name of the value passed doesn't have to match
def get_area(shape):
    # Switch to lowercase for easy comparison
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


# Create function that calculates the rectangle area
def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))

    area = length * width

    print("The area of the rectangle is", area)


# Create function that calculates the circle area
def circle_area():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    # Format the output to 2 decimal places
    print("The area of the circle is {:.2f}".format(area))

'''










# recursive function dict

mydict={"name":"hanqing","age":"21"}
#print(mydict)

'''

def factorial(num):
    if num<=1:
        return 1
    else:
        result=num*factorial(num-1)
        return result
#print (factorial(4))

# how to print out 1 1 2 3 5 8 13 21??/

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        result=fib(n-1)+fib(n-2)
        return result
print(fib(7))
'''




