print('LINEAR SEARCH')
l=[12,3,5,37,44,65]
print(l)
x=int(input('enter the element: '))
for i in range(0,len(l)):
    #print('i',i,'ele:',l[i])
    if x==l[i]:
        print('index : ',i)
        break
    else:
        continue

print('BINARY SEARCH')
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1

arr = [ 2, 3, 4, 10, 40 ]
print(arr)
x=int(input('enter the el : '))
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

