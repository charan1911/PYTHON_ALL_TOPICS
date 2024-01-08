print('-----------SET IN PYTHON----------')
print('..........SETS BASICS..........')
print("..........UNORDERED , NO DUP's , UNCHANGEABLE..........")
set0={'a',1,False}
print('PRINTING OF SET : ',set0)
print('LENGTH OF SET IS len(SET_NAME) : ',len(set0))
print('TYPE OF SET IS type(SET_NAME) :',type(set0))
print('THE CONSTRUCTOR IS USED FOR THIS IS ---> set() ')
print('WE CAN ACCESS THROUGH LOOPS/COND../IF')
print()
print('APPENDING / UPDATING')
set1={'a',1,True,'a','b'}
set1.add('c')
print('ADDING ELE TO THE SET : ',set1)
set2={'x','y','z'}
set2.update(set1)
print('UPDATING SET2 WITH SET1 : ',set2)
#print('-WE CAN UPDATE 1 SET TO OTHER LIST,TUPLE,SET ALSO-') DOUBT????
print()
print('RENOVE / DISCARD FROM SET')
my_set = {1, 2, 3, 4, 5}
my_set.remove(2)
print('REMOVING 2 FROM SET : ',my_set)
print('''IF WE TRYING REMOVE NON THERE ELEMENT : REMOVE SHOW ERROR
DISCARD WONT SHOW ERROR''')
my_set.discard(2)
print('DISCARDING 2 FROM SET : ',my_set)
print("")
print()
removed_element = my_set.pop()
print("BEFORE POP'ING SET : ",my_set)
print("AFTER POP'ING SET : ",removed_element)
print()
print('\\\\\\--JOINING THE SETS--\\\\\\')
print('''IN JOINING : UPDATE SET2 WITH SET1 WILL s2.update(s1),
UNION WILL CREATE NEW SET BY COMBINING SET1 AND SET2''')
s1={'A','B'}
s2={'C','D'}
print('s1 : ',s1,'and s2 : ',s2)
s1.update(s2)
print('UPDATING S1 AND S2 :',s1)
print()
s3=s1.union(s2)
print('UNION S1 AND S2 IN S3---->','S1 : ',s1,"S2 : ",s2,"S3 : ",s3)
s4={'A','B'}
s5={'C','D','A'}
print("S4 : ",s4,"S5 : ",s5)
s4.intersection_update(s5)
print('the intersection_update() will gives common value :',s4)
print()
s6={'a','b'}
s7={'x','y'}
print("S6 : ",s6,"S7 : ",s7)
s=s6.intersection(s7)
print('the intersetion() method will gives the all values in both',s)
print()
print('''<s1.symmetric_difference_update(s2)> will update s1 with uncommon ele from both sets,
<s1.symmetric_difference(s2)> will uncommon ele in new set s3''')

print()
print('METHODS IN SETS (17)')
print('''
update(),
union()
symmetric_difference_update(),
symmetric_difference(),
remove(),
pop(),
issuperset(),
issubset(),
isdisjoint(),
istersection_update(),
istersection(),
discard(),
difference_update(),
difference(),
copy(),
clear(),
add()
''')
print()
print()
print('--------------------------------------------------------------------------')

      
      
