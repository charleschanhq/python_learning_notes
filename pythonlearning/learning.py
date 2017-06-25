from decimal import Decimal

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










