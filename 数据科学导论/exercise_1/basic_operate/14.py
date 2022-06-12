def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
arr = [88,5,23,31,45,4,6,1,16,12]
print ("原数组:")
for i in arr:
    print (i,end=" ")
sort(arr)
print ("\n排序后的数组:")
for i in arr:
    print (i,end=" ")