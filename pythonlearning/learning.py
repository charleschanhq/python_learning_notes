from decimal import Decimal
import math
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