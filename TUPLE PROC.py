print("----------TUPLE IS ORDERED , UNCHANGEABLE AND ALLOW DUP'S----------")
print("")
print("..........TUPLE BASICS..........")
tuple1=('a',1,True,'a','b')
print('..........TUPLE ALLOWS ONLY THIS DATATYPES.......... : ',tuple1)
print('..........TYPE OF TUPLE.......... : ',type(tuple1))
print('..........LENGTH.......... : ',len(tuple1))
print('..........VALUE OF INDEX 0.......... : ',tuple1[0])
print('..........VALUE OF INDEX -1.......... : ',tuple1[-1])
print('..........VALUES FROM 1 TO 5(5-1).......... : ',tuple1[1:5])
print('..........ALSO WE CAN GET LIKE ---> [s:][:e][s:e][-s:][:-e][-s:-e]..........')
print("")
print("")
print("----------SINGLE TUPLE VS STRING----------")
tuple_new=('a')
print('TAKES AS ONLY SINGLE STRING---> ',tuple_new,"IS : ",type(tuple_new))
tuple_new=('a',)
print('TAKES AS ONLY SINGLE STRING WITH COMMA---> ',tuple_new,'IS : ',type(tuple_new))
print('---we can use constructor tuple()---')
print()
print()
print('----------CONVERTING TO TUPLE----------')
tuple1=tuple([1,'w',True])
tuple2=(('a','b','c'))
tuple3=({True,False})
print('TUPLE : ',tuple1," ITS TYPE : ",type(tuple1))
print('TUPLE : ',tuple2," ITS TYPE : ",type(tuple2))
print('TUPLE : ',tuple3," ITS TYPE : ",type(tuple3))
print("")
print("")
print('----------POINTS----------')
print('---WE CAN USE CONDITIONS LIKE -->  LOOPS,IF,WHILE---')
print('''.....WE CAN DO CHANGES,ADDING,REMOVING,DELETION BY CHANGE TUPLE
TO LIST AND THEN AGAIN IN TO TUPLE AFTER PERFORMATION.....''')
print("")
print("")
print('----------APPENDING VALUES TO UNCHANGEABLE TUPLE----------')
tuple_new1=('a',)
print('before append : ',tuple_new1)
tuple_new1=list(tuple_new1)
print('before append CONVERTED : ',tuple_new1)
tuple_new1.append('b')
print('before append CONVERTED : ',tuple_new1)
tuple_new1=tuple(tuple_new1)
print("")
print("")
print("----------ALGEBRAIC OPERATIONS ON TUPLES----------")
print('after append FINAL : ',tuple_new1)
tuple_new2=(1,2)
tuple_new3=('a',)
print('appending two tuple into one',tuple_new2,tuple_new3)
print("ADDING TWO TUPLES INTO ONE : ",tuple_new2+tuple_new3)
print("MULTILICATION OF TUPLE WITH 9 : ",tuple_new2*2)
print("")
print("")
print('----------UNPACKING TUPLE----------')
tuple_example = ('a', 1, True)
print(tuple_example)
# Unpack the tuple into individual variables
alpha, number, boolean = tuple_example
print("alpha, number, boolean = tuple_example")
# Print the unpacked values
print('alpha:', alpha)
print('number:', number)
print('boolean:', boolean)
print("")
print("")
print('----------TUPLES METHODS----------')
my_tuple = (1, 2, 2, 3, 'a', 'b')
print("my_tuple : ",my_tuple)
print("my_tuple count of no:2 like tuple_name.count(ele to count) : ",my_tuple.count(2))      # Output: 2
print("my_tuple index of no:2 like tuple_name.index(ele in that index) : ",my_tuple.index('a'))    # Output: 4
print('--------------------------------------------------')
