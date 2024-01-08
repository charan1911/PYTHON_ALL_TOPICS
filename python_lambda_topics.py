print('\\\\\\--LAMBDA IN PYTHON and ARRAY--\\\\\\')
n=11
n1=0
n2=1
for i in range(1,1+n):
    if i==1:
        print(i,":",1)
    else:
        n3=n2+n1
        print(i,':',n3)
        n1=n2
        n2=n3
        x=n3
print(f'{n}th fib number: {x}')
x=lambda a:a+5

print('adding output lambda function with 1.arg:a=5 ,+5 ',x(5))
x=lambda a,b:a+5+b
print('adiing lambda function with 2.arg:a=2 b=3 ,+5 :',x(2,3))
def lam(n):
    
    return lambda a:a*n
my=lam(2)
print('doubles the number using lambda passed to my var:',my(50))
print('PRINTING FIB SERIES USING DEF FUNCTION')
print('------------------------------')
def lamm(m):
    n1=0
    n2=1
    for i in range(1,1+n):
        if i==1:
            print(i,':',1)
        else:
            n3=n2+n1
            print(i,':',n3)
            n1=n2
            n2=n3           
lamm(11)
print('-------------------------------')
print()
print('ARRAY IS SAME LIKE LISTS WITH ITS METHODS')






    

    
     
 
 

    
