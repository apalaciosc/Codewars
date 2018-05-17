def min_sum(arr):
    # Your code here
    arr.sort()
    i=0
    c=0
    suma=0
    while c<len(arr)/2:
    	suma=suma+arr[c]*arr[i-1]
    	i-=1
    	c+=1
    return suma

print(min_sum([5,4,2,3]))