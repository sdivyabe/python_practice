num = [1,2,3,4,5,6,7,8,9,10]

op = [i for i in num]
nw = [i for i in num if i == 1]
print(op)
print(nw)

sq = [i*i for i in num]
print(sq)

odd = [i for i in num if i%2 != 0]
print(odd)

div = [i for i in num if i%2 !=0 and i%3 == 0 ]
print(div)

numbers = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
outerlist = []
innerlist = []
for i in numbers:
    for j in i:  
        if j%2 !=0: 
           innerlist.append(j) 
    # print(innerlist)
        outerlist.append(innerlist)
print(outerlist)