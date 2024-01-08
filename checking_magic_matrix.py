'''n=3
l1=[]
for i in range(n):
    l2=[]
    for j in range(n):
        no=int(input('enter the number : '))
        l2.append(no)
    l1.append(l2)
print(l1)
'''
r1,r2,r3=0,0,0
c1,c2,c3=0,0,0
d1,d2=0,0
l1=[[6,1,8],
    [7,5,3],
    [2,9,4]]
l2=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print(l1)
print(' ')
print(l2)
print(' ')
n=int(input('enter 1 0r 2 :'))
l3=[]
if n==1:
    l3=l1
elif n==2:
    l3=l2
    

for i in range(3):
    if i==0:
        for j in range(3):r1+=l3[i][j]
        #print('r1 : ',r1)
    elif i==1:
        for j in range(3):r2+=l3[i][j]
        #print('r2 : ',r1)
    elif i==2:
        for j in range(3):r3+=l3[i][j]
        #print('r3 : ',r1)

for i in range(3):
    if i==0:
        for j in range(3):c1+=l3[j][i]
        #print('c1 : ',c1)
    elif i==1:
        for j in range(3):c2+=l3[j][i]
        #print('c2 : ',c2)
    elif i==2:
        for j in range(3):c3+=l3[j][i]
        #print('c3 : ',c3)


for i in range(3):
    if i==0:
        for j in range(3):
            if j==1 or j==2:
                continue
            else:
                #print(l3[i][j])
                d1+=l3[i][j]
    elif i==1:
        for j in range(3):
            if j==0 or j==2:
                continue
            else:
                #print(l3[i][j])
                d1+=l3[i][j]
    elif i==2:
        for j in range(3):
            #print(l3[i][j])
            if j==0 or j==1:
                continue
            else:
                #print(l3[i][j])
                d1+=l3[i][j]
#print('d1 : ',d1)

for i in range(3):
    if i==0:
        for j in range(3):
            if j==0 or j==1:
                continue
            else:
                #print(l3[i][j])
                d2+=l3[i][j]
    elif i==1:
        for j in range(3):
            if j==0 or j==2:
                continue
            else:
                #print(l3[i][j])
                d2+=l3[i][j]
    elif i==2:
        for j in range(3):
            if j==1 or j==2:
                continue
            else:
                #print(l3[i][j])
                d2+=l3[i][j]
#print('d1 : ',d1)

if r1==r2==r3==c1==c2==c3==d1==d2:
    print('yes')
else:
    print('no')
