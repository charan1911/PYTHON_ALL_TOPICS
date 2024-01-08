'''def merge(left,right):
    print('left m                                 :',left)
    print('right m                                :',right)
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
            print('result if                            :',result)
        else:
            result.append(right[j])
            j+=1
            print('result else                            :',result)
    result+=left[i:]
    print('result remaining in i-list to append   :',result)
    result+=right[j:]
    print('result remaining in j-list to append   :',result)
    return result


def mergesort(lst):
    print('length                                 :' ,len(lst))
    if(len(lst)<=1):
        print('leng                                   :',len(lst))# to print list if there is only 1 element...
        print('list                                   :',lst)
        return lst
    mid = int(len(lst)/2)
    print('mid                                    :',mid)
    left=mergesort(lst[:mid])
    print('left                                   :' ,left)
    #print('left : ',left)
    right=mergesort(lst[mid:])
    print('right                                  :',right)
    return merge(left,right)

arr=[9,8,7,6,5]
print('LAST AND FINAL SORTED LIST             :',mergesort(arr))
'''



import math as m
'''print('SELECTION SORT IN PYTHON')
l1=[99,29,72,98,13,87,66,52,51,36]
print('LIST BEFORE SORT :',l1)
for i in range(0,len(l1)):
    for j in range(i,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print('LIST AFTER SORT :',l1)
print()
print()
"""li=[29,72,98,13,87,66,52,51,36]
print('BUBBLE SORT IN PYTHON')
print('list before sort : ',li)
co=0
while True:
    if l[co]>l[co+1]:
        l[co],l[co+1]=l[co+1],l[co]
        print(l[co],l[co+1])
print(l)
"""
l2=[1000,9,1,8,5,2]
print('LIST BEFORE SORT :',l2)
for i in range(len(l2)):
    for j in range(len(l2)-1):
        if l2[j]>l2[j+1]:
            #print('after : ',li[j],li[j+1])
            l2[j],l2[j+1]=l2[j+1],l2[j]
            #print('before : ',li[j],li[j+1])
print('LIST AFTER SORT :',l2)
print()
print()
l3=[100,9,1,8,5,2]
print('LIST BEFORE SORT :',l3)
for i in range(len(l3)):
    for j in rang7e(len(l3)-1):
        if l3[j]>l3[j+1]:
            #print('after : ',li[j],li[j+1])
            l3[j],l3[j+1]=l3[l3.index(l3[j+1])],l3[l3.index(l3[j])]
            #print('before : ',li[j],li[j+1])
print('LIST AFTER SORT :',l3)

'''
print('SELECTION AND INSERTION SORT ARE SIMILAR ALGORITHM')
l=[9,1,8,6,5]
print('')
print('SELECTION SORT IN PYTHON')
print('list before sort :',l)
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print('list after sort :',l)
print('')
print('BUBBLE SORT IN PYTHON')
a=[9,8,7,6,5]
print('before sort : ',a)
#print(len(l))
for i in range(len(a),0,-1):
    for i in range(i-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print('after sort : ',a)
        




























