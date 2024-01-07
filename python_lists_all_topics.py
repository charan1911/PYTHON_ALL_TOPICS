l=[1,1,1.0,'a',True]
print("DATA TYPES IN LIST : ",l)
print('')
print("LIST LENGTH ",l,'IS : ',len(l))
print('')
print("INDEX 0 VALUE IN ",l," IS : ",l[0])
print('')
print("INDEX -1 VALUE ",l,"IS : ",l[-1])
print('')
print('PRINTING ELE FROM _ TO LEN-1 : ',l[:(len(l)-1)])
print('')
print('PRINTING ELE FROM _ TO -1 : ',l[:-1])
print('')
print("PRINTING ELE FORM -VE TO +VE : ",l[-(10):])
print('')
print('LAST ELE --> -VE : ',l[-(len(l))])
print('')
print('ELE FROM -VE TO _ : ',l[-1:])
print('')
print('ELE FROM -VE TO _ : ',l[-5:])


print('')
print("CHECKING NUMBER IS THER IN LIST OR NOT !!!")
if 1 in l:
    print('YES 1 IS THERE !!')
if 2 not in l:
    print('NO 2 NOT THERE !!')

print("")
print("CHANGING ELE IN LIST FROM A TO AA")
print("BEFORE CHANGE : ",l)
l[3]='aa'
print("AFTER CHANGE : ",l)

print("")
print("CHANGING ELE IN LIST SET OF INDEXES")
print("BEFORE CHANGE : ",l)
l[0:2]=[11,11]
print("AFTER CHANGE : ",l)
print("")
print("ADD NESTED LIST IN SPECIFIC INDEX")
print("BEFORE CHANGE : ",l)
l[2]=[1.0,1.0]
print("AFTER CHANGE : ",l)
print("")
print("ADD ELE FROM SLICE TO SLICE")
print("BEFORE CHANGE : ",l)
l[2:3]=['bb','bb']
print("AFTER CHANGE : ",l)
print("")
print("ADD SINGLE ELE FROM SLICE TO SLICE")
print("BEFORE CHANGE : ",l)
l[2:4]='1'
print("AFTER CHANGE : ",l)
print("")
print("ADD ELE IN SPECIFIED INDEX")
print("BEFORE CHANGE : ",l)
l.insert(2,'hello')
print("AFTER CHANGE : ",l)
print("")
print("APPEND LIST INTO LIST AS NESTED LIST ")
l.append(['z'])
print(l)
print("")
print("APPEND ELE AS A ELE INTO LIST")
l.append('m')
print(l)
print("")
print("APPEND TUPLE IN THE LIST")
l.append(('e'))
print(l)
print("")
print("EXTEND ADD ELEMENTS AS INDIVIDUALLY WITH LIST")
l.extend(['x','y','z'])
print(l)
print("")
print("EXTEND ADD ELEMENTS AS INDIVIDUALLY WITH TUPLE unchangable!!")
l.extend(('e','f','g','g',1,1.0,True))
print(l)
print("")
print("EXTEND ADD ELEMENTS AS INDIVIDUALLY WITH SET no duplicates!!")
l.extend({'e','f','g','g',1,1.0,True})
print(l)
print("")
print("REMOVE METHOD remove SPECIFIC ELEMENTS FROM LIST")
print("BEFORE CHANGE : ",l)
l.remove('hello')
print("AFTER CHANGE : ",l)
print("")
print("POP WILL REMOVE FROM LIST and GIVES THE VALUE OF SPECIFIED INDEX !!")
pop=l.pop(5)
print('value at specified index "5" : ',pop)
print("")
print("DEL METHOD WILL DELETE VALUE FROM LIST WIL SPECIFIED INDEX")
print("BEFORE CHANGE : ",l)
del l[5]
print("AFTER CHANGE : ",l)
print("")
print("CLEAR METHOD WILL CLEAR THE LIST BY REMOVING ALL ELE IN IT !!")
print("BEFORE CHANGE : ",l)
l.clear()
print("AFTER CHANGE : ",l)
print("")
print("----DEL METHOD WILL DELETE THE ENTIRE LIST AND ITS ELE !!----")
del l
print("")
print("")

print("we can perform for loop,range with len or num,while and in condition")

ff = ['a','b','c','d','f','f']
print("list : ",ff)
newlist = [x for x in ff if "a" in x]
print("ONLY GIVES ELE THAT CONTAINS LETTER 'A' specified")
print(newlist)
print("")
print("ONLY GIVES ELE THAT NOT CONTAINS LETTER 'F' specified")
fruits = ['a','b','c','d','f','f']
newlist = [x for x in fruits if x != "f"]
print(newlist)
print("")
print("GIVES ALL ELE IN LIST")
fruits = ['a','b','c','d','f','f']
newlist = [x for x in fruits]
print(newlist)
print("")
print("GIVES NUMBER IN THE RANGE OF 10 specified")
newlist = [x for x in range(10)]
print(newlist)
print("")
print("GIVES NUMBERS THAT ARE LESS THAN 5 specified")
newlist = [x for x in range(10) if x < 5]
print(newlist)
print("")
print("USING UPPER METHOD THE ELE WILL CONVERT INTO CAPITALS")
fruits = ['a','b','c','d','f']
newlist = [x.upper() for x in fruits]
print(newlist)
print("")
print("IT GIVES THE MSG IF IT SATISIFY THE CONDITION PERFORMED ON LIST ELE")
fruits = ["apple", "banana", "cherry", "kiwi", "mango",'orange']
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print("")
#print('appending elements to other in one line in cmmt line')
a=['a','b','y','z','c']
b=[1,2,900,99]
print("NORMAL NUMBER AND ALPHABET LISTS")
print(a,'\n',b)
a.sort()
b.sort()
print("NORMAL NUMBER AND ALPHABET LISTS AFTER SORTING !!!!")
print(a,'\n',b)
a.sort(reverse=True)
b.sort(reverse=True)
print("NORMAL NUMBER AND ALPHABET LISTS AFTER REVERSING !!!!")
print(a,'\n',b)
print("")
print("IT SORT THE NUMBERS ACCORDING TO THE ABS with myfun DEFINITION!!!")
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print("")#IT IS FOR SPACE IN OUTPUT FOR BETTER VIEWING....
a=[1,2,3]
print("A : ",a)
print("")#IT IS FOR SPACE IN OUTPUT FOR BETTER VIEWING....
print("WITH COPY FUNCTION B VAR STORE A ARRAY VALUE !!!")
b=a.copy()
print("B : ",b)
print("")#IT IS FOR SPACE IN OUTPUT FOR BETTER VIEWING....
print("IT IS SAME LIKE COPY BUT IT CREATE NEW LIST IN C VAR !!!")
c=list(a)
print(c)
print("")#IT IS FOR SPACE IN OUTPUT FOR BETTER VIEWING....
print("")#IT IS FOR SPACE IN OUTPUT FOR BETTER VIEWING....
print("")#IT IS FOR SPACE IN OUTPUT FOR BETTER VIEWING....
print('''
append()----------Adds an element at the end of the list
clear()-----------Removes all the elements from the list
copy()------------Returns a copy of the list
count()-----------Returns the number of elements with the specified value
extend()----------Add the elements of a list (or any iterable), to the end of the current list
index()-----------Returns the index of the first element with the specified value
insert()----------Adds an element at the specified position
pop()-------------Removes the element at the specified position
remove()----------Removes the item with the specified value
reverse()---------Reverses the order of the list
sort()------------Sorts the list ''')
print('OTHER METHODS THAT CAN BE PERFORMED ON LIST!!!')

