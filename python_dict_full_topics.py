print('\\\\\\--DICTIONARY TOPICS--\\\\\\')
print('----CHANGEABLE,NO DUPLICATES,VALUES ACCESS WITH KEYS----')
d={'a':'apple','b':'ball','c':'cat'}
print('printing dictionary: ',d)
print('printing value with key --> "b" : ',d['b'])
print('--DUPLICATE CALUES WILL OVERWRITE THE EXISTING VALUE--')
print('gives length of dictionary :',len(d))
print('the value for key may be any datatype and list,set,tuple,etc..')
print('type of this datatype will :',type(d))
print("")
print(d)
d=dict(a='applee',b='balll',c='cat')
print("dict method from a='applee',b='balll',c='cat' to ",d)
print()
print('\\\\\\--ACCESS ITEMS--\\\\\\')
#print('WE CAN ACCESS WITH KEY OR WITH get() --> d.keys() METHOD')
d={'a':'apple','b':'ball',
   'c':'cat'}
print('WE CAN GET KEYS OF DICTIONARY WITH keys() --> d.keys() method:',d.keys())
print('WE CAN GET VALUES OF DICTIONARY WITH values() --> d.values method: ',d.values())
print('WE CAN GER KEY:VALUES OF DICTIONARY WITH items() --> d.items() : ',d.items())
print("")
d={'a':'apple','b':'ball','c':'cat'}
print('before adding new element: ',d)
d['d']='dog'
print('after adding new element: ',d)
print("")
print("------------OVERWRITING----------")
d={'a':'apple','b':'ball','c':'cat'}
print('before overwriting :',d)
d['a']='anaconda'
print('after overwriting :',d)
print()
print('\\\\\\--UPDATING VALUES IN DICTIONARY--\\\\\\')
d={'a':'apple','b':'ball','c':'cat'}
print('before update :',d)
d.update({'b':'bat'})
print('after update :',d)
print()
print()
d={'a':'apple','b':'ball','c':'cat'}
print('\\\\\\--DELETING THE ITEMS FROM DICTIONARY--\\\\\\')
print('the pop() method will remove with specified key name :')
print('before pop() method :',d)
d.pop('c')
print('after pop() method :',d)
print("")
print('--THE popitem() method REMOVE THE LAST ITEM/RANDOM ITEM FROM DICTIONARY--')
print("")
print('THE del keyword WILL REMOVE THE SPECIFIED VALUES/ENTIRE FROM DICTIONARY')
print("")
print('THE clear() keyword WILL CLEAR THE WHOLE DICTIONARY')
print("")
print('THE copy()/dict(dict variable) method WILL COPY THE DICT TO OTHER VARIABLE')
print("")
print('THE DICTIONARY SUBTOPICS NESTED DICT: DICT WITH-IN DICT')
print("")
print('\\\\\\--DICTIONARY METHODS--\\\\\\')
print('''
----------clear(),
----------copy(),
----------fromkeys()
----------get(),
----------items(),
----------keys(),
----------pop(),
----------popitem(),
----------setdefault(),
----------update(),
----------values()
''')











    
