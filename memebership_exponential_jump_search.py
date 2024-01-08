
print('------MEMBERSHIP OPERATION------')
print('''
this is a topic uses the 'in' or 'is not' ...,so on''')
print(' ')

print('------EXPONENTIAL SEARCH------')
def binarySearch( arr, l, r, x):
    print('l = ',l,'r = ',r)
    if r >= l:
        mid = l + ( r-l ) // 2
        print(mid)
        if arr[mid] == x:
            print('arr[mid] = ',arr[mid],'x = ',x)
            return mid
        if arr[mid] > x:
            print('arr[mid] = ',arr[mid],'x = ',x)
            return binarySearch(arr, l,mid - 1, x)
        return binarySearch(arr, mid + 1, r, x)
    return -1

def exponentialSearch(arr, n, x):
	if arr[0] == x:
		return 0
	i = 1
	print('i = ',i,'n = ',n,'arr[i] = ',arr[i],'x = ',x)
	while i < n and arr[i] <= x :
		i = i * 2
		print('i = ',i)
	return binarySearch( arr, i // 2,min(i, n-1), x)
    
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)
if result == -1:
	print ("Element not found in the array")
else:
	print ("Element is present at index %d" %(result))


print('------JUMP SEARCH------')
print('''
its the same as exponential search but it will just with exponent
of 2 and in jump search the search element will jump untill element
is greater than find element and do linear search there .''')
