print('\\\\\\--CLASS CREATION AND FUNCUTION CREATION--\\\\\\')
print('CREATING CLASS')
class class1:
    def __init__(self,name,age):
        self.peru=name
        self.vayasu=age
    def __str__(self):
        return f"{self.peru}({self.vayasu})"
x=class1('BOBBY',20)
print('output coming because of __str__ function in class :',x)
print('output coming after arguments passed with var x & printing name :',x.peru)
print('printing name and age by giving values in print statement :',class1('CHARAN',20).peru)
class class2:
    def jan26():
        ans=input('s to run,other then s to stop : ')
        while ans=='s':
            if ans=='s':
                name=input('give name : ')
                print('printing name and age by giving values in print statement :',class1(name,19).peru)
            ans=input('s to run,other then s to stop : ')
        return 'printed cuz answer is no , and came out of loop'
  
joiner=class2.jan26()
print(joiner)
cls1=class1('platinum',1119)
print(cls1)
print('WE CAN MODIFY/DELECT THE OBJECT PROPERTIES AND PASS STATEMENTS')



    

    
     
 
 

    


    

    
     
 
 

    
