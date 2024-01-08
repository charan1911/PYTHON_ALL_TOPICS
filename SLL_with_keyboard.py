class node:
    def __init__(self,data):
        self.data=data
        self.next=None      
class sll():  
    def __init__(self,n):
        self.head=None
        num=n
        print(num)    
    def display(self):
        if self.head==None:
            print('empty linked list...')
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                temp=temp.next


print('PRINTING DEFAULT NUMBER IN SLL')
l=sll('WELCOME TO THE SINGLE LINKED LIST...')
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
l.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
l.display()


print('\n')
print('PRINTING KEYS FROM USER & GETTING VALUES FROM DICTIONARY')
l=sll('WELCOME TO THE SINGLE LINKED LIST...')     
ll={'16':'charan','58':'prabhu','a0':'shree','52':'nikhil'}
n1=node(ll[input('enter : ')])
n2=node(ll[input('enter : ')])
n3=node(ll[input('enter : ')])
n4=node(ll[input('enter : ')])
l.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
l.display()


print('\n')  
print('PRINTING N VALUES INPUT FROM USER OF MONTHS ')
l=sll('WELCOME TO THE SINGLE LINKED LIST...')    
n=int(input('''PRINTING VALUES TAKING KEYS FROM USER AND GETTING VALUES
            FROM DICTIONARY : '''))
for i in range(1,n+1):
    z={1:'january',
       2:'february',
       3:'march',
       4:'april',
       5:'may',
       6:'june',
       7:'july',
       8:'august',
       9:'september',
       10:'october',
       11:'november',
       12:'december'}
    if l.head==None:
        n1=node(z[int(input('enter : '))])
        l.head=n1 
           
        temp=n1
    else:
        n1=node(z[int(input('enter : '))])
        temp.next=n1
        temp=n1

        
l.display()







