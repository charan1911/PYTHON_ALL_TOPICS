class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def display(self,n):
        if self.head==None:
            print('circular linked list is empty')
        else:
            temp=self.head
            while temp and n:
                print(temp.data,end=' ')
                temp=temp.next
                n-=1
n=cll()
n1=node(10)
n2=node(20)
n3=node(30)

n.head=n1
n1.next=n2
n2.next=n3
n3.next=n1

n.display(int(input('enter the no of circular linked list to print :' )))
