import random #python default package

""" print("Hi");

x=int(input("Enter the number"))
print(type(x));
y=x+1;
print(type(y));
print(x,y);


print(random.randrange(2,45)) """

#String Datatypes - is a combination of numbers, characters, spacial char and white spaces anything that enclose in qoutes
#=================

""" a = "Welcome Divya"
print(type(a[2])) #output l
print(type(a[2:])) #output lcome Divya
print(type(a[:5])) #output Welco
len(a) # output 13 (including spaces)
 """
""" text = 'Welcome'
print("welcome" in text) #output False
print("welcome" in text.lower()) #output True
print([*text]) #loop method(output - w,e,l,c,o,m,e)
print(list(text)) #loop method(output - w,e,l,c,o,m,e)
print(text.upper())
print(text.replace('e','f'))
 """
#for x in range(5): #output - 0,1,2,3,4

#Query optimization 
#===================
""" 
x= 10
t = "Welcome FDS - {}"
print(t.format(x)) #output - Welcome FDS - 10

x=10
y= 'python class'
t = "Welcome FDS - {1} {0}"
print(t.format(y,x))

# \"\" - escape character
print("Hi \"Divya\"") """

#To get the multiple input from user and print the sum of it
#------------------------------------------------------------

""" user = [] # or user = list()
sum1 = 0;

for i in range(5): #indentation, using whitespace, to define scope; such as the scope of loops, functions and classes.(no need of curly braces)
    b=int(input("Enter the Values:"))
    user.append(b)
    sum1=sum1+b
    print(user)
    print(sum1) """

# List Examples
#----------------

""" listItem = ['a','b','c',1,2]
listItem.append('divya')
print(listItem)
len(listItem) """

""" a = {}
n=int(input("Enter the number"))
for i in range(n):
    b=input("Enter the name")
    a.update('name',b)
   
print(a) """

""" a = 2
b = 3
c = (a+b)**2
print (c)
d = (a**2)+(b**2)+(2*a*b)
print(d)
 """

""" a = int(input("enter number : "))
b = int(input("enter number : "))

c = (a+b)**2
d = (a**2)+(b**2)+(2*a*b)

if c == d:
    print("Equal")
else:
    print("Not equal")

 """

""" str = input('Enter the String : ')
con = 0
spl = ['@','#','$','&']
for i in str :
    if 'a'== i or 'e' == i or 'i' == i:
        print("vowels")
    else :
        print(i)
 """
""" str = input('Enter the String : ')
spl = ['@','#','$','&']
con = ""

for i in range(len(str)) :
    if str[i] not in spl:
        con = con + str[i]
    print(con) """

name = input("Enter the Name :")
splChar = ['@','#','$','&',' ','%','*','/','|','?']
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cons = ''
for i in range(len(name)):
    if name[i] not in vow:
        if name[i] not in splChar:
            if not str[i].isdigit():
                cons = cons+ name[i]
print("After removing : ",cons)