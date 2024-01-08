print('''STACK IN PYTHON ''')
print('it can perform by removing last element 1st with pop() function')
n=int(input('enter the length of stack you want to be : '))
l=[]
for i in range(n):
    ll=int(input())
    l.append(ll)
print("appended to stack : ",l)
for i in range(n+1):
    if len(l)!=0:
        print("pop'ed from stack : ",l.pop())
    else:
        print('empty stack :',l)

print('QUEUE IN PYTHON')
print('it can perform by removing first element 1st with pop(0) with in index 0')
n=int(input('enter the length of queue you want to be : '))
l=[]
for i in range(n):
    ll=int(input())
    l.append(ll)
print("added to queue : ",l)
for i in range(n+1):
    if len(l)!=0:
        print("pop'ed from queue : ",l.pop())
    else:
        print('empty queue :',l)
