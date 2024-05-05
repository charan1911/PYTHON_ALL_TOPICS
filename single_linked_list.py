class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class sll():
    
    def __init__(self,n):
        self.head=None
        print(n)
    def display(self):
        if self.head==None:
            print('empty linked list...')
        else:
            temp=self.head
            while temp:
                print('aaa',temp.data,end=' ')
                temp=temp.next

l=sll('WELCOME TO THE SINGLE LINKED LIST...')


n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)

l.head=n1
n1.next=n2
n3.next=n4
n2.next=n3
 
l.display()
i=input()
if i=="n2":
   n2.next=n4
l.display()


