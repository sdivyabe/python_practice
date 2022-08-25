""" str = input("Enter the string : ")
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print("vowels")
    else: print(i)
 """
str = input("Enter the string : ")
splChar = ['!','@','#','$','%','^','&','*','+','-','_',' ','|','?','/']
vowels = ['a','e','i','o','u','A','E','I','O','U']
cons = ''
for i in range(len(str)):
    if str[i] not in splChar:
        if str[i] not in vowels:
            if not str[i].isdigit():
                cons = cons + str[i]
print('After Removing', cons)
