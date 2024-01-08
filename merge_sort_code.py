def merge(left,right):
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
