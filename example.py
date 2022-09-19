num = [1,2,3,4,5,6,7,8,9,10]

def even():
    for i in range(len(num)):
        if num[i] % 2 == 0:
            print ('even numbers',num[i])
            sq = num[i]*num[i]
            print(sq)
        else: print('hi')
even()

op = [i*i for i in num if i%2 == 0]
print(op)

name = input("Enter the Name")
vowel = ['a','e','i','o','u','A','E','I','O','U']
con = ''
def vowels():
    for i in range(len(name)):
        print("hi")
        if name[i] not in vowel:
            print("bye")
            con = con + name[i]
            print(con)
vowels()