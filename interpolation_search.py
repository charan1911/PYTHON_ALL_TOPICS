
def interpolationSearch(arr, lo, hi, x):
    print('lo :',lo,'hi : ',hi,'x : ',x,'arr[lo] : ',arr[lo],'arr[hi] : ',arr[hi])
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *(x - arr[lo]))
        print(pos)
        if arr[pos] == x:
            print('==')
            return pos
        if arr[pos] < x:
            print('<')
            return interpolationSearch(arr, pos + 1,hi, x)
        if arr[pos] > x:
            print('>')
            return interpolationSearch(arr, lo,pos - 1, x)
        return -1
arr = [10,12,13,16,18,19]
n = len(arr)
x = 18
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
	print("Element found at index", index)
else:
	print("Element not found")

print('''it is like linear search with in recursive calling of function
      one by one in list and compare it with (x) element to get equal.
      ''')
